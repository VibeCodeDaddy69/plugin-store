
# kamino-lend -- Skill Summary

## Overview
This skill provides complete interaction with Kamino Lend, Solana's leading lending protocol, enabling users to view markets, manage lending positions, supply assets for yield, withdraw funds, borrow against collateral, and repay loans. All operations include transaction previews and require explicit user confirmation for write operations, with comprehensive error handling and health factor monitoring to prevent liquidation risks.

## Usage
Install the plugin and use commands like `kamino-lend markets` to view lending rates, `kamino-lend positions` to check your obligations, and `kamino-lend supply --token USDC --amount 0.01` to earn yield. All write operations require `--confirm` flag after previewing transaction details.

## Commands
| Command | Description |
|---------|-------------|
| `kamino-lend markets` | View all lending markets with APYs and TVL |
| `kamino-lend positions` | Check your lending obligations and health factor |
| `kamino-lend supply --token <TOKEN> --amount <AMOUNT>` | Supply assets to earn yield |
| `kamino-lend withdraw --token <TOKEN> --amount <AMOUNT>` | Withdraw supplied assets |
| `kamino-lend borrow --token <TOKEN> --amount <AMOUNT> --dry-run` | Preview borrowing against collateral |
| `kamino-lend repay --token <TOKEN> --amount <AMOUNT> --dry-run` | Preview loan repayment |

## Triggers
Activate this skill when users ask about Kamino lending rates, want to check their lending positions, need to supply/withdraw assets for yield, or want to borrow/repay on Kamino Lend. Use for any Kamino lending protocol interactions on Solana.
