// src/onchainos.rs — onchainos CLI wrapper
use std::process::Command;
use serde_json::Value;

/// Query current logged-in wallet address via wallet addresses.
pub fn resolve_wallet(chain_id: u64) -> anyhow::Result<String> {
    let chain_str = chain_id.to_string();
    let output = Command::new("onchainos")
        .args(["wallet", "addresses", "--chain", &chain_str])
        .output()?;
    let json: Value = serde_json::from_str(&String::from_utf8_lossy(&output.stdout))
        .map_err(|e| anyhow::anyhow!("wallet addresses parse error: {}", e))?;
    let addr = json["data"]["evm"][0]["address"].as_str().unwrap_or("").to_string();
    Ok(addr)
}

/// Submit an on-chain call via onchainos wallet contract-call.
/// dry_run=true returns a simulated response without calling onchainos.
/// NOTE: onchainos wallet contract-call does NOT support --dry-run; we handle it here.
pub async fn wallet_contract_call(
    chain_id: u64,
    to: &str,
    input_data: &str,
    from: Option<&str>,
    amt: Option<u128>,
    dry_run: bool,
) -> anyhow::Result<Value> {
    if dry_run {
        return Ok(serde_json::json!({
            "ok": true,
            "dry_run": true,
            "data": { "txHash": "0x0000000000000000000000000000000000000000000000000000000000000000" },
            "calldata": input_data
        }));
    }

    let chain_str = chain_id.to_string();
    let mut args = vec![
        "wallet", "contract-call",
        "--chain", &chain_str,
        "--to", to,
        "--input-data", input_data,
    ];

    let amt_str;
    if let Some(v) = amt {
        amt_str = v.to_string();
        args.extend_from_slice(&["--amt", &amt_str]);
    }
    let from_str;
    if let Some(f) = from {
        from_str = f.to_string();
        args.extend_from_slice(&["--from", &from_str]);
    }
    let output = Command::new("onchainos").args(&args).output()?;
    let stdout = String::from_utf8_lossy(&output.stdout);
    Ok(serde_json::from_str(&stdout).unwrap_or_else(|_| serde_json::json!({
        "ok": false,
        "error": stdout.to_string()
    })))
}

/// Extract txHash from wallet contract-call response: data.txHash
pub fn extract_tx_hash(result: &Value) -> &str {
    result["data"]["txHash"]
        .as_str()
        .or_else(|| result["txHash"].as_str())
        .unwrap_or("pending")
}

/// Poll eth_getTransactionReceipt until the tx is mined (up to ~60s), then
/// return Err if the receipt shows status 0x0 (reverted). This prevents
/// false-success reporting when a broadcast tx reverts on-chain.
pub async fn wait_and_check_receipt(tx_hash: &str, rpc_url: &str) -> anyhow::Result<()> {
    let client = reqwest::Client::new();
    let body = serde_json::json!({
        "jsonrpc": "2.0",
        "method": "eth_getTransactionReceipt",
        "params": [tx_hash],
        "id": 1
    });

    for attempt in 0..12u32 {
        if attempt > 0 {
            tokio::time::sleep(std::time::Duration::from_secs(5)).await;
        }
        let resp: Value = match client.post(rpc_url).json(&body).send().await {
            Ok(r) => match r.json().await {
                Ok(v) => v,
                Err(_) => continue,
            },
            Err(_) => continue,
        };

        let result = &resp["result"];
        if result.is_null() {
            continue; // not mined yet
        }

        let status = result["status"].as_str().unwrap_or("0x0");
        if status == "0x0" || status == "0" {
            anyhow::bail!(
                "Transaction {} reverted on-chain (status=0x0). \
                 Check slippage tolerance or amounts and retry.",
                tx_hash
            );
        }
        return Ok(());
    }

    // Timed out — warn but don't hard-fail
    eprintln!(
        "  [warn] Could not confirm receipt for {} within 60s — verify on-chain before assuming success.",
        tx_hash
    );
    Ok(())
}

/// ERC-20 approve — no onchainos dex approve command; manually encode calldata.
/// approve(address,uint256) selector = 0x095ea7b3
pub async fn erc20_approve(
    chain_id: u64,
    token_addr: &str,
    spender: &str,
    amount: u128,
    from: Option<&str>,
    dry_run: bool,
) -> anyhow::Result<Value> {
    let spender_padded = format!("{:0>64}", spender.trim_start_matches("0x").trim_start_matches("0X"));
    let amount_hex = format!("{:064x}", amount);
    let calldata = format!("0x095ea7b3{}{}", spender_padded, amount_hex);
    wallet_contract_call(chain_id, token_addr, &calldata, from, None, dry_run).await
}
