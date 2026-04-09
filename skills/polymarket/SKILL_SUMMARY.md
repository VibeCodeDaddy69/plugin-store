
# polymarket -- Skill Summary

## Overview
This skill enables trading on Polymarket prediction markets through Polygon. Users can browse markets, buy/sell YES/NO outcome tokens, manage positions, and cancel orders. The plugin uses local EIP-712 signing for order authentication and automatically handles USDC.e approvals for trades. All market data comes from Polymarket's CLOB, Gamma, and Data APIs.

## Usage
Install the plugin and connect your wallet to Polygon (chain 137). Trading commands auto-generate local credentials on first use. Browse markets with `list-markets`, place orders with `buy`/`sell`, and monitor positions with `get-positions`.

## Commands
| Command | Description |
|---------|-------------|
| `list-markets` | Browse active prediction markets with optional filtering |
| `get-market` | Get detailed market info and order book by ID or slug |
| `get-positions` | View open positions and P&L for wallet address |
| `buy` | Purchase YES/NO shares with USDC.e |
| `sell` | Sell existing YES/NO shares |
| `cancel` | Cancel open orders by ID, market, or all orders |

## Triggers
Activate when users want to trade prediction markets, check Polymarket positions, browse prediction markets, or manage Polymarket orders. Also triggered by phrases like "polymarket shares," "prediction market trade," or "buy yes token."
