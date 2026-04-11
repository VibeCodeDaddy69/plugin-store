
# gmx-v2 -- Skill Summary

## Overview
This skill enables trading perpetual futures and managing liquidity on GMX V2, a leading decentralized perpetuals exchange. Users can open leveraged long/short positions, place conditional orders, and participate in GM liquidity pools on Arbitrum and Avalanche networks. The plugin handles all complex interactions with GMX's keeper-based execution model, providing safety checks and clear confirmation flows.

## Usage
Connect your wallet with `onchainos wallet login`, then use commands like `gmx-v2 open-position` for trading or `gmx-v2 deposit-liquidity` for LP operations. Always run with `--dry-run` first to preview transactions before execution.

## Commands
| Command | Description |
|---------|-------------|
| `list-markets` | View active GMX V2 markets with liquidity and rates |
| `get-prices` | Get current oracle prices for all tokens |
| `get-positions` | Query open perpetual positions |
| `get-orders` | Query pending conditional orders |
| `open-position` | Open leveraged long/short position |
| `close-position` | Close existing position (full or partial) |
| `place-order` | Place limit/stop-loss/take-profit orders |
| `cancel-order` | Cancel pending conditional order |
| `deposit-liquidity` | Add liquidity to GM pools |
| `withdraw-liquidity` | Remove liquidity from GM pools |
| `claim-funding-fees` | Claim accrued funding fee income |

## Triggers
Activate when users want to trade perpetuals with leverage, manage GMX positions, place stop-losses or take-profits, or participate in GMX liquidity mining. Common phrases include "open position GMX", "GMX leverage", "GMX stop loss", or "deposit GM pool".
