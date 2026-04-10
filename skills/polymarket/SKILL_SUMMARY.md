
# polymarket -- Skill Summary

## Overview
This skill enables trading on Polymarket prediction markets on Polygon, where users can buy and sell outcome tokens (YES/NO or categorical) that resolve to $1.00 for winning outcomes and $0.00 for losing ones. It supports market browsing, position checking, order placement, and order management through Polymarket's central limit order book (CLOB) system, with automatic credential derivation from the onchainos wallet.

## Usage
Install the polymarket plugin and ensure onchainos CLI is installed for trading operations. The skill automatically derives API credentials from your onchainos wallet on first trade, requiring no manual setup.

## Commands
| Command | Description |
|---------|-------------|
| `list-markets` | Browse active prediction markets with optional keyword filtering |
| `get-market` | Get detailed market information and order book data |
| `get-positions` | View open positions and P&L for wallet address |
| `buy` | Buy outcome shares with USDC.e (market or limit orders) |
| `sell` | Sell outcome shares (market or limit orders) |
| `cancel` | Cancel orders by ID, market, or all orders |

## Triggers
Activate when users want to trade prediction markets, check polymarket positions, browse markets by topic, or manage existing orders on Polymarket. Use for any prediction market trading activity on Polygon involving YES/NO or categorical outcome tokens.
