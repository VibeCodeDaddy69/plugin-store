
# compound-v3 -- Skill Summary

## Overview
This plugin provides comprehensive access to Compound V3 (Comet) lending markets across multiple chains. It enables users to supply collateral, borrow base assets, repay debt, withdraw collateral, and claim COMP rewards. The plugin includes safety features like dry-run previews, overflow protection for repayments, and automatic debt repayment when supplying base assets.

## Usage
Install via OKX plugin store, ensure onchainos wallet is connected, then use compound-v3 commands with appropriate chain and market parameters. All write operations require user confirmation after dry-run preview.

## Commands
| Command | Description |
|---------|-------------|
| `get-markets` | View market statistics (utilization, APRs, totals) |
| `get-position` | View account position (balances, collateral status) |
| `supply` | Supply collateral or base asset to the market |
| `borrow` | Borrow base asset using supplied collateral |
| `repay` | Repay borrowed base asset (full or partial) |
| `withdraw` | Withdraw supplied collateral (requires zero debt) |
| `claim-rewards` | Claim available COMP rewards |

## Triggers
Activate when users mention compound lending operations, borrowing against collateral, repaying debt, checking compound positions, or claiming compound rewards. Also trigger for phrases like "compound supply", "compound borrow", "compound repay", "compound withdraw", or "compound rewards".
