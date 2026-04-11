
# etherfi -- Skill Summary

## Overview
The etherfi skill enables liquid restaking on Ethereum through the ether.fi protocol. Users can deposit ETH to receive eETH (liquid staking tokens), wrap eETH into weETH (ERC-4626 yield-bearing tokens) that auto-compound rewards from both Ethereum staking and EigenLayer restaking, and manage their positions including withdrawals through a two-step process. The skill provides real-time APY tracking and portfolio monitoring capabilities.

## Usage
Run `etherfi positions` to view current balances and APY. All write operations require `--confirm` flag after previewing the transaction details first.

## Commands
- `positions` - View eETH/weETH balances and protocol APY (read-only)
- `stake --amount <ETH>` - Deposit ETH to receive eETH tokens
- `wrap --amount <eETH>` - Convert eETH to yield-bearing weETH
- `unwrap --amount <weETH>` - Convert weETH back to eETH
- `unstake --amount <eETH>` - Request ETH withdrawal (step 1)
- `unstake --claim --token-id <id>` - Claim finalized ETH withdrawal (step 2)

## Triggers
Activate when users want to stake ETH on ether.fi, manage eETH/weETH positions, check liquid restaking yields, or perform withdrawals from the ether.fi protocol. Also triggered by requests for EigenLayer restaking or liquid staking alternatives.
