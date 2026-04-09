
# pancakeswap-v2 -- Skill Summary

## Overview
This skill enables interaction with PancakeSwap V2, the constant-product (xyk) automated market maker on BSC and Base networks. It provides comprehensive functionality for token swapping, liquidity provision, and pool data retrieval, with built-in safety features including transaction previews, slippage protection, and explicit user confirmation for all write operations.

## Usage
Use voice commands like "swap USDT for CAKE on PancakeSwap V2" or "add liquidity to CAKE/BNB pool" to trigger operations. All write operations require explicit user confirmation after displaying transaction previews via dry-run mode.

## Commands
| Command | Description |
|---------|-------------|
| `quote` | Get expected swap output amounts and pricing |
| `swap` | Execute token swaps with slippage protection |
| `add-liquidity` | Provide liquidity to earn LP tokens |
| `remove-liquidity` | Withdraw liquidity by burning LP tokens |
| `get-pair` | Look up pair contract addresses |
| `get-reserves` | Check current pool reserves and ratios |
| `lp-balance` | View LP token balances for specific pairs |

## Triggers
Activate this skill when users want to trade tokens, provide liquidity, or check prices on PancakeSwap V2 specifically (not V3). Trigger phrases include "swap on pancakeswap v2", "add liquidity pancakeswap", "pancake amm", and "check pancake pair".
