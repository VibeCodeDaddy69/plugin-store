
# polymarket -- Skill Summary

## Overview
This skill enables trading on Polymarket prediction markets on Polygon, where users can buy and sell outcome tokens for real-world events. Markets resolve to $1.00 for winning outcomes and $0.00 for losing outcomes, with prices representing implied probabilities. The plugin supports browsing markets, checking positions, placing buy/sell orders with USDC.e, and managing orders through Polymarket's CLOB (Central Limit Order Book) system.

## Usage
Install the polymarket binary and connect your onchainos wallet to Polygon (chain 137). Use read-only commands like `list-markets` and `get-positions` without authentication, or trade with `buy`/`sell` commands that automatically derive API credentials from your wallet.

## Commands
| Command | Description |
|---------|-------------|
| `list-markets` | Browse active prediction markets with optional keyword filtering |
| `get-market` | Get detailed market info and order book by ID or slug |
| `get-positions` | View open positions with P&L for wallet address |
| `buy` | Buy outcome shares using USDC.e with limit or market orders |
| `sell` | Sell outcome shares with limit or market orders |
| `cancel` | Cancel open orders by ID, market, or all orders |

## Triggers
Activate this skill when users want to trade prediction markets, check Polymarket positions, browse betting odds on real-world events, or manage open orders on outcome tokens. Ideal for phrases like "buy polymarket shares," "check my positions," or "what are the odds on [event]."
