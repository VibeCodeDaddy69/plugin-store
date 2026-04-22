# macro-intelligence
Unified macro intelligence feed that reads 7 sources (NewsNow, Polymarket, OpenNews, Finnhub, Telegram, FRED, Fear & Greed), classifies events with regex + LLM, scores sentiment, and exposes filtered signals via HTTP API for downstream trading skills.

## Highlights
- 7 data sources: NewsNow, Polymarket, 6551.io OpenNews, Finnhub, Telegram, FRED, Fear & Greed Index
- 3-layer classification: keyword regex → LLM confirm (ambiguous) → LLM discover (missed keywords)
- 24+ event types with bilingual patterns: Fed cuts/hikes, CPI, gold, geopolitical, tariffs, whale alerts, RWA catalysts
- Token Impact Engine: each macro signal maps to specific crypto tokens with directional impact scores (23 event types + generic fallback)
- Source diversity guarantee: min 5 signals per source type, returns 80 diverse signals instead of letting one source flood the feed
- Macro playbook maps each event to direction, magnitude, and urgency for downstream consumption
- Sender reputation system with 30-day decay — high-rep sources get 1.3x magnitude boost
- FRED hard indicators: Fed Funds Rate, CPI, GDP, Unemployment, 10Y-2Y spread, 10Y yield
- 11 HTTP API endpoints for filtered signals, sentiment, regime, Polymarket, and price tickers
- Neon-glass terminal dashboard with heat column, sparklines, token impact pills, and pulse effects
- No trading logic — read-only intelligence feed; all sources degrade gracefully without API keys
