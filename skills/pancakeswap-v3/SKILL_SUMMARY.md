
# pancakeswap-v3 -- Skill Summary

## Overview
This skill enables token swaps and concentrated liquidity management on PancakeSwap V3 across multiple chains including BNB Chain, Base, Ethereum, Arbitrum, and Linea. It provides comprehensive DEX functionality including price quotes, token swaps via SmartRouter, liquidity position creation and removal, pool analysis, and portfolio tracking. The skill handles complex V3 mathematics, multi-step transaction flows, and cross-chain contract interactions while ensuring proper slippage protection and balance validation.

## Usage
Install the binary via the auto-injected script, ensure your wallet is connected with `onchainos wallet login`, then use commands like `pancakeswap-v3 swap` or `pancakeswap-v3 add-liquidity` with appropriate parameters. All write operations require `--confirm` flag for execution.

## Commands
- `quote` - Get swap quotes without executing transactions
- `swap` - Execute token swaps via SmartRouter (requires --confirm)
- `pools` - List all pools for a token pair across fee tiers
- `positions` - View LP positions for a wallet address
- `add-liquidity` - Mint new concentrated liquidity positions (requires --confirm)
- `remove-liquidity` - Remove liquidity and collect tokens (requires --confirm)

## Triggers
Activate this skill when users mention PancakeSwap operations, token swapping, liquidity provision, or DEX interactions on supported chains. Common trigger phrases include "pancakeswap", "swap tokens", "add liquidity", "remove liquidity", or "check pools".
