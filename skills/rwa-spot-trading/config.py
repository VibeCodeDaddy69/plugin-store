"""
RWA Alpha — Real World Asset Intelligence Trading Skill 配置文件
修改此文件调整策略参数，无需改动 rwa_alpha.py
"""
import json, os

# ── 运行模式 ────────────────────────────────────────────────────────────
MODE              = "paper"
PAUSED            = False
STRATEGY_MODE     = "full_alpha"

# ── 资金分配 ────────────────────────────────────────────────────────────
TOTAL_BUDGET_USD  = 1000
MAX_POSITIONS     = 6                 # 最多同时持仓数
MAX_SINGLE_PCT    = 25                # 单一代币最大占比 (%)
MAX_CATEGORY_PCT  = 50                # 单一类别最大占比 (%)
BUY_AMOUNT_USD    = 100

# ── 链配置 ──────────────────────────────────────────────────────────────
ENABLED_CHAINS    = ["ethereum"]
CHAIN_CONFIG      = {
    "ethereum":  {"chain": "ethereum",  "chain_index": "1",        "stable": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},  # USDC
    "bsc":       {"chain": "bsc",       "chain_index": "56",       "stable": "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d"},  # USDC
    "solana":    {"chain": "solana",    "chain_index": "501",      "stable": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"},  # USDC
    "arbitrum":  {"chain": "arbitrum",  "chain_index": "42161",    "stable": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831"},  # USDC
    "mantle":    {"chain": "mantle",    "chain_index": "5000",     "stable": "0x09Bc4E0D10E52d372d242C5a50DcEe1B0838E533"},  # USDC
    "linea":     {"chain": "linea",     "chain_index": "70000080", "stable": "0x176211869cA2b568f2A7D4EE941E073BEd8F1024"},  # USDC
    "tron":      {"chain": "tron",      "chain_index": "195",      "stable": "TEkxiTehnzSmSe2XqrBj4w32RUN966rdz8"},          # USDT
    "aptos":     {"chain": "aptos",     "chain_index": "607",      "stable": ""},  # TBD
}
GAS_RESERVE       = {"ethereum": 0.01, "solana": 0.02, "bsc": 0.005, "arbitrum": 0.001}

# ── 感知层 (Perception) ────────────────────────────────────────────────
NEWS_POLL_SEC     = 120               # 新闻/宏观事件检查周期 (秒)
CHAIN_POLL_SEC    = 60                # 链上状态刷新周期 (秒)
SENTIMENT_WINDOW  = 7                 # 情绪移动平均窗口 (天)

# ── LLM 辅助分类 (Headline Classification) ────────────────────────────
LLM_ENABLED       = True              # True=启用 LLM 辅助分类, False=仅关键词
LLM_MODEL         = "claude-haiku-4-5-20251001"  # 最便宜最快的模型
LLM_CONFIDENCE_BAND = (0.55, 0.80)   # 只对这个 conviction 区间调用 LLM
                                       # >0.80 = 关键词已够明确, <0.55 = 噪音

# ── 认知层 (Cognition) ─────────────────────────────────────────────────
MIN_CONVICTION    = 0.55              # 最低信号置信度才交易 (0.0~1.0)
NAV_ZSCORE_ENTRY  = 1.5              # NAV 套利入场 z-score 阈值
YIELD_ROTATION_BPS = 50               # 收益率轮换最小差值 (bps)
MACRO_OVERRIDE    = 0.80              # 宏观事件高于此值直接覆盖其他信号

# ── 执行层 (Execution) ─────────────────────────────────────────────────
SLIPPAGE_BUY      = 1.0               # 买入滑点 (%)
SLIPPAGE_SELL     = 2.0               # 卖出滑点 (%)

# ── 风控 ───────────────────────────────────────────────────────────────
MAX_DAILY_TRADES  = 10                # 每日最大交易次数
SESSION_STOP_USD  = 50                # 累计亏损停止交易 (USDC)
COOLDOWN_LOSS_SEC = 300               # 亏损后冷却 (秒)
MAX_DRAWDOWN_PCT  = 8                 # 投资组合级止损 (%)
MIN_LIQUIDITY_USD = 200_000           # 最小池流动性 (RWA 代币通常流动性更高)
MAX_NAV_PREMIUM_BPS = 50              # 不买 NAV 溢价 >50bps 的代币

# ── 止盈止损 (资产锚定型: USDY, OUSG, PAXG, sDAI) ────────────────────
TP_NAV_PREMIUM_BPS = 40              # NAV 溢价超 40bps 止盈
SL_NAV_DISCOUNT_BPS = 100            # NAV 折价超 100bps 止损

# ── 止盈止损 (治理代币型: ONDO, CFG, MPL, PENDLE, PLUME, OM, GFI, TRU) ──
TP_GOVERNANCE_PCT = 20                # +20% 止盈
SL_GOVERNANCE_PCT = -10               # -10% 止损
TRAILING_ACTIVATE = 10                # 追踪止损: 盈利超 10% 激活
TRAILING_DROP     = 8                 # 追踪止损: 峰值回撤 8% 触发

# ── 止盈止损 (代币化股票: xstock, ondo_tokenized, stablestock, etc.) ──
TP_EQUITY_PCT     = 15                # +15% 止盈
SL_EQUITY_PCT     = -8                # -8% 止损

# ── 收益率轮换 ─────────────────────────────────────────────────────────
YIELD_CHECK_SEC   = 3600              # 收益率对比检查周期 (秒)
MIN_YIELD_ADV_PCT = 0.50              # 最小 APY 优势才轮换 (%)

# ── Dashboard ──────────────────────────────────────────────────────────
DASHBOARD_PORT    = 3249

# ── RWA 代币宇宙 (data-file driven) ──────────────────────────────────
# Loaded from JSON at startup. native_rwa.json overrides rwa_universe.json on collision.
# category: treasury / gold / defi_yield / rwa_gov / yield_protocol / rwa_infra / rwa_credit
#           xstock / ondo_tokenized / stablestock / prestock / rstock / leveraged
# asset_backed: True = asset-backed, False = governance/utility
# has_nav: True = NAV premium/discount arbitrage (treasury, gold, defi_yield)

_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

def _load_universe():
    universe = {}
    extended = os.path.join(_DATA_DIR, "rwa_universe.json")
    native = os.path.join(_DATA_DIR, "native_rwa.json")
    if os.path.exists(extended):
        with open(extended, encoding="utf-8") as f:
            universe.update(json.load(f))
    if os.path.exists(native):
        with open(native, encoding="utf-8") as f:
            universe.update(json.load(f))  # native overrides
    return universe

RWA_UNIVERSE = _load_universe()

CATEGORY_NAMES = {
    "treasury":         "Tokenized Treasury",
    "gold":             "Tokenized Gold",
    "defi_yield":       "DeFi Yield",
    "rwa_gov":          "RWA Governance",
    "yield_protocol":   "Yield Protocol",
    "rwa_infra":        "RWA Infrastructure",
    "rwa_credit":       "RWA Credit",
    "xstock":           "xStock (Backed.fi)",
    "ondo_tokenized":   "Ondo Tokenized",
    "stablestock":      "Stablestock",
    "prestock":         "PreStocks",
    "rstock":           "rStock",
    "leveraged":        "Leveraged ETF",
}

# ── 轮询分层 (Polling Tiers) ─────────────────────────────────────────
POLL_TIER_0_SEC   = 60                # Tier 0: held positions + active signals
POLL_TIER_1_SEC   = 300               # Tier 1: native RWA + top 20 by liquidity
POLL_TIER_2_SEC   = 1800              # Tier 2: extended universe (955 tokens)
POLL_BATCH_SIZE   = 10                # Concurrent price fetches per batch
NATIVE_RWA_SYMBOLS = [
    "USDY", "OUSG", "sDAI", "bIB01", "PAXG", "XAUT",
    "USDe", "ONDO", "CFG", "MPL", "PENDLE", "PLUME", "OM", "GFI", "TRU",
]

# ── 稳定币忽略列表 ────────────────────────────────────────────────────
_IGNORE_TOKENS = {
    "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",  # USDC (ETH)
    "0xdAC17F958D2ee523a2206206994597C13D831ec7",  # USDT (ETH)
    "0x6B175474E89094C44Da98b954EedeAC495271d0F",  # DAI  (ETH)
    "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", # USDC (SOL)
}
