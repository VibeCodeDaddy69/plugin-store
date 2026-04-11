
# clanker -- Skill Summary

## Overview
The clanker skill enables users to deploy and manage Clanker ERC-20 tokens on Base and Arbitrum networks. It provides comprehensive token lifecycle management including deployment with built-in MEV protection and LP fee structures, discovery through creator-based search, and reward claiming capabilities. All operations include automatic security scanning and work directly with on-chain contracts without requiring external API keys.

## Usage
Install with `npx skills add clanker --global`, ensure `onchainos` is logged in, and use commands like `clanker deploy-token` to launch tokens or `clanker list-tokens` to browse recent deployments. Write operations require user confirmation and sufficient ETH for gas fees.

## Commands
| Command | Description |
|---------|-------------|
| `list-tokens` | List recently deployed Clanker tokens with filtering and pagination |
| `search-tokens --query <address\|username>` | Search tokens by creator address or Farcaster username |
| `token-info --address <addr>` | Get on-chain token metadata and price information |
| `deploy-token --name X --symbol Y` | Deploy new ERC-20 token via Clanker V4 factory |
| `claim-rewards --token-address <addr>` | Claim LP fee rewards for deployed tokens |

## Triggers
Activate when users want to deploy tokens ("launch token on Clanker", "create token on Base"), search for existing tokens ("show tokens by creator", "list latest tokens"), or manage rewards ("claim LP rewards", "collect creator fees"). Use for Clanker-specific token operations on Base and Arbitrum networks.
