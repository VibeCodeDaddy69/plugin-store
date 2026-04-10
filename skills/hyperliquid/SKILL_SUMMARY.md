
# hyperliquid -- Skill Summary

## Overview
This skill enables AI agents to interact with Hyperliquid, a high-performance on-chain perpetuals exchange built on its own L1 blockchain. It provides comprehensive trading functionality including position management, order placement with TP/SL brackets, market data retrieval, and USDC deposits from Arbitrum. All operations are executed on Hyperliquid L1 (chain ID 999) with full on-chain settlement in USDC, offering CEX-like speed with decentralized transparency.

## Usage
First run `hyperliquid register` to set up your signing address for order operations. Use `hyperliquid positions` to check your current positions and `hyperliquid prices --market BTC` to get market prices. All write operations (order, close, cancel) require `--confirm` flag after previewing the action.

## Commands
- `hyperliquid register` - Set up signing address for trading operations
- `hyperliquid positions [--address] [--show-orders]` - Check open positions and account summary
- `hyperliquid prices [--market COIN]` - Get current market prices
- `hyperliquid order --coin COIN --side buy/sell --size SIZE [--type limit] [--price PRICE] [--sl-px PRICE] [--tp-px PRICE] [--confirm]` - Place perpetual orders with optional TP/SL
- `hyperliquid close --coin COIN [--size SIZE] [--confirm]` - Market close positions
- `hyperliquid tpsl --coin COIN [--sl-px PRICE] [--tp-px PRICE] [--confirm]` - Set stop-loss/take-profit on existing positions
- `hyperliquid cancel --coin COIN --order-id ID [--confirm]` - Cancel open orders
- `hyperliquid deposit --amount USD_AMOUNT [--confirm]` - Deposit USDC from Arbitrum

## Triggers
Activate this skill when users want to trade perpetuals on Hyperliquid, check positions, manage orders, or interact with the Hyperliquid DEX. Common trigger phrases include "trade on Hyperliquid", "check my HL positions", "Hyperliquid long/short", "set stop loss", or "deposit to Hyperliquid".
