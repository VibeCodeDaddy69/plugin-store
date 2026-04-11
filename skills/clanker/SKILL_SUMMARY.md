
# clanker -- Skill Summary

## Overview
The clanker skill enables deployment and management of ERC-20 tokens through the Clanker protocol on Base and Arbitrum networks. It provides comprehensive token lifecycle management including deployment with automated liquidity provision, creator search functionality, token discovery, and LP fee reward claiming. All deployments include MEV protection, automated WETH pairing, and configurable fee structures.

## Usage
Install the clanker binary and ensure onchainos CLI is logged in with sufficient ETH for gas fees. Use trigger phrases like "deploy token", "search Clanker tokens", or "claim LP rewards" to activate token operations.

## Commands
| Command | Description |
|---------|-------------|
| `list-tokens` | List recently deployed Clanker tokens with pagination |
| `search-tokens --query <address\|username>` | Search tokens by creator address or Farcaster username |
| `token-info --address <addr>` | Get on-chain token metadata and price information |
| `deploy-token --name X --symbol Y` | Deploy new ERC-20 token via Clanker V4 factory |
| `claim-rewards --token-address <addr>` | Claim LP fee rewards for deployed tokens |

## Triggers
Activate when users want to deploy tokens on Base/Arbitrum, search for tokens by creator, check token prices/info, or claim LP rewards from Clanker deployments. Do not use for buying/selling tokens or non-Clanker deployments.
