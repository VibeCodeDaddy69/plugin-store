**Overview**

Deploy ERC-20 tokens on Base via Clanker's AI-native launchpad — each token is automatically paired with WETH on Uniswap V3 at launch, and the deployer earns LP fees from every trade.

**Prerequisites**
- onchainos agentic wallet connected
- Base wallet (chain 8453) with at least 0.001 ETH for deployment gas
- Reward claiming also supported on Arbitrum One (42161)

**How it Works**
1. **Browse recent launches**: See recently deployed tokens and their on-chain metadata. `clanker-plugin list-tokens --limit 10`
2. **Search by creator**: Find tokens launched by a specific wallet or username. `clanker-plugin search-tokens --query <wallet-or-username>`
3. **Get token details**: View supply, Uniswap V3 pool address, and accrued LP fees for a token. `clanker-plugin token-info --address <contract>`
4. **Deploy a token**: Launch your ERC-20 — it's immediately paired with WETH on Uniswap V3 and tradeable. `clanker-plugin deploy-token --name "My Token" --symbol MTK --image-url <url> --confirm`
5. **Claim LP rewards**: Withdraw accumulated WETH trading fees from your token's pool to your wallet. `clanker-plugin claim-rewards --token-address <contract> --confirm`
