
# morpho -- Skill Summary

## Overview
Morpho is a permissionless lending protocol with over $5B TVL operating on two layers: Morpho Blue isolated lending markets and MetaMorpho ERC-4626 vaults curated by risk managers. Users can supply assets to earn yield, borrow against collateral, and manage positions with health factor monitoring across Ethereum Mainnet and Base networks.

## Usage
Install with `npx skills add okx/plugin-store-community --skill morpho`, then connect your wallet via `onchainos wallet login`. Always use `--dry-run` first for write operations, then confirm before executing on-chain.

## Commands
| Command | Description |
|---------|-------------|
| `morpho positions` | View your positions and health factors |
| `morpho markets [--asset SYMBOL]` | List Morpho Blue markets with APYs |
| `morpho vaults [--asset SYMBOL]` | List MetaMorpho vaults |
| `morpho supply --vault ADDR --asset SYMBOL --amount N` | Supply to MetaMorpho vault |
| `morpho withdraw --vault ADDR --asset SYMBOL --amount N` | Withdraw from vault |
| `morpho borrow --market-id HEX --amount N` | Borrow from Morpho Blue |
| `morpho repay --market-id HEX --amount N` | Repay debt |
| `morpho supply-collateral --market-id HEX --amount N` | Add collateral |
| `morpho claim-rewards` | Claim Merkl rewards |

## Triggers
Activate when users mention supplying/depositing to Morpho vaults, borrowing from Morpho Blue, checking positions or health factors, viewing interest rates, repaying loans, or managing collateral. Also trigger on phrases like "earn yield on morpho", "morpho markets", or "metamorpho vaults".
