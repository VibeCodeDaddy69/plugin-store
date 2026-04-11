
# raydium -- Skill Summary

## Overview
This plugin provides comprehensive access to Raydium's automated market maker (AMM) on Solana, enabling users to execute token swaps, query real-time prices, and access detailed pool information. It integrates directly with Raydium's REST APIs and Solana mainnet, offering both read-only operations for price discovery and write operations for actual token swapping with built-in safety mechanisms.

## Usage
Install the plugin and use commands like `raydium get-swap-quote` for price discovery or `raydium swap` for executing trades. Always preview swaps with `--dry-run` and confirm with users before executing on-chain transactions.

## Commands
| Command | Description |
|---------|-------------|
| `get-swap-quote` | Get expected output amount and price impact for a token swap |
| `get-price` | Calculate price ratio between two tokens |
| `get-token-price` | Get USD price for one or more tokens |
| `get-pools` | Query pool information by token pairs or pool IDs |
| `get-pool-list` | Get paginated list of all Raydium pools |
| `swap` | Execute token swap on-chain (requires user confirmation) |

## Triggers
Activate when users want to swap tokens on Raydium, check token prices, or explore liquidity pools on Solana. Common trigger phrases include "swap on raydium," "raydium price," "get swap quote," or "raydium pool info."
