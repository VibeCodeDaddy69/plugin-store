# market-structure-analyzer
Crypto market-structure research agent delivering institutional-grade analysis
with 24+ indicators across derivatives, options, on-chain, smart money, and
macro sentiment — powered by OKX CeFi CLI + OnchainOS, zero pip dependencies.

## Highlights
- Live auto-refreshing dashboard with K-line candlestick charts (TradingView Lightweight Charts v4)
- TA overlays: RSI (14), MACD (12/26/9), Bollinger Bands (20, 2σ) with timeframe selector
- 12-signal composite scoring engine (-100 to +100) with real-time updates
- 20+ real-time indicators: funding, OI, basis, taker volume, L/S ratios, liquidation pressure, realized vol, Fear & Greed, BTC dominance, stablecoin dry powder
- Options quant (Tier 1): gamma wall, 25-delta skew, ATM IV, butterfly spread
- On-chain: MVRV ratio + realized price (CoinMetrics), smart money signals + DEX hot tokens (OnchainOS)
- Dune Analytics: exchange flows, whale transfers, stablecoin CEX flows (4 pre-built queries, optional)
- Multi-token support: BTC/ETH (full), SOL/BNB/DOGE/AVAX/ARB/XRP/LINK (Tier 2), PEPE (Tier 3)
- Glass morphism UI with fetch activity indicators and 3s price ticker
- Python stdlib only — zero pip dependencies
