
# pendle
Pendle Finance yield tokenization plugin for trading principal tokens (PT), yield tokens (YT), and providing AMM liquidity across multiple chains.

## Highlights
- Buy/sell PT tokens to lock in fixed yield rates
- Trade YT tokens for floating yield exposure
- Add/remove single-token AMM liquidity 
- Mint/redeem PT+YT pairs from underlying assets
- Support for Ethereum, Arbitrum, BSC, and Base
- Real-time market data and position tracking
- Integrated ERC-20 approval handling
- Dry-run capability for transaction preview

---SEPARATOR---

# pendle -- Skill Summary

## Overview
This skill enables interaction with Pendle Finance's yield tokenization protocol, allowing users to split yield-bearing assets into principal tokens (PT) for fixed yield and yield tokens (YT) for floating yield exposure. It supports trading these tokens, providing AMM liquidity, and managing positions across Ethereum, Arbitrum, BSC, and Base networks through direct API integration and on-chain transaction execution.

## Usage
Run pre-flight checks with `pendle --version` and `onchainos wallet status` to ensure setup is complete. Use `--dry-run` flag for transaction preview before executing any write operations that require user confirmation.

## Commands
| Command | Purpose |
|---------|---------|
| `list-markets` | Browse available Pendle markets and pools |
| `get-market` | Get detailed market information and APY data |
| `get-positions` | View current PT/YT/LP positions |
| `get-asset-price` | Check token prices for PT, YT, LP, or SY tokens |
| `buy-pt` | Purchase principal tokens for fixed yield |
| `sell-pt` | Sell principal tokens back to underlying |
| `buy-yt` | Purchase yield tokens for floating yield exposure |
| `sell-yt` | Sell yield tokens back to underlying |
| `add-liquidity` | Provide single-token liquidity to AMM |
| `remove-liquidity` | Withdraw liquidity from AMM pools |
| `mint-py` | Mint PT+YT pairs from underlying assets |
| `redeem-py` | Redeem PT+YT pairs back to underlying |

## Triggers
Activate when users want to trade fixed vs floating yield, manage Pendle positions, or interact with yield tokenization. Key phrases include "buy PT", "sell YT", "Pendle liquidity", "fixed yield", "mint PT YT", and "Pendle positions".
