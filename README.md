# GridWorld Value Iteration Implementation

## Problem Description

This project implements a value iteration algorithm for a 4x4 GridWorld environment where:

- An agent starts at the top-left corner (state 0)
- The goal is to reach the bottom-right corner (state 15)
- The agent can move in four directions (up, down, left, right) with equal probability (0.25)
- Each move incurs a reward of -1
- The terminal state (bottom-right) has a reward of 0
- There are no obstacles in the environment

## Implementation Details

The solution implements the Bellman equation iteratively until convergence:

1. Initialization:
   - Grid size: 4x4
   - Rewards: -1 for each move, 0 for terminal state
   - Initial value function V(s) = 0 for all states
   - Discount factor (gamma) = 1.0 (no discounting)
   - Convergence threshold (theta) = 1e-4

2. Value Iteration Process:
   - For each state (excluding terminal state)
   - For each possible action (up, down, left, right)
   - Calculate next state considering boundary conditions
   - Update values using the Bellman equation
   - Track maximum change in values
   - Continue until convergence (max change < threshold)

## Console Output

After running the value iteration algorithm, the final value function converges to:

```
[[-59.42367735 -57.42387125 -54.2813141  -51.71012579]
 [-57.42387125 -54.56699476 -49.71029394 -45.13926711]
 [-54.2813141  -49.71029394 -40.85391609 -29.99766609]
 [-51.71012579 -45.13926711 -29.99766609   0.        ]]
```

This matrix represents the expected cumulative reward for each state in the grid. The values show that states closer to the goal (bottom-right) have higher values, which is expected as they require fewer steps to reach the terminal state.
