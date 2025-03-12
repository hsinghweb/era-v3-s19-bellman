import numpy as np

def gridworld_value_iteration():
    # 1. Initialize parameters
    N = 4  # Grid size (4x4)
    gamma = 1.0  # Discount factor (no discounting)
    theta = 1e-4  # Convergence threshold
    
    # Initialize value function to zeros
    V = np.zeros((N, N))
    
    # Define rewards: -1 for each move, 0 for terminal state
    rewards = np.full((N, N), -1)
    rewards[N-1, N-1] = 0  # Terminal state has 0 reward
    
    # Define actions: up, down, left, right
    actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 3. Value iteration
    iteration = 0
    while True:
        iteration += 1
        # Track maximum change in value
        delta = 0
        
        # Create a copy of current value function
        V_new = np.copy(V)
        
        # For each state
        for i in range(N):
            for j in range(N):
                # Skip terminal state (bottom-right corner)
                if i == N-1 and j == N-1:
                    continue
                
                # Initialize expected value for this state
                expected_value = 0
                
                # For each action
                for action in actions:
                    # Find next state coordinates
                    ni, nj = i + action[0], j + action[1]
                    
                    # Handle boundary conditions (stay in the same state if would go outside grid)
                    if ni < 0 or ni >= N or nj < 0 or nj >= N:
                        ni, nj = i, j
                    
                    # Probability of taking each action (equal probability 0.25)
                    p = 0.25
                    
                    # Add expected value contribution from this action
                    expected_value += p * (rewards[i, j] + gamma * V[ni, nj])
                
                # Update value function
                V_new[i, j] = expected_value
                
                # Update maximum change
                delta = max(delta, abs(V_new[i, j] - V[i, j]))
        
        # Update value function
        V = np.copy(V_new)
        
        # Check for convergence
        if delta < theta:
            break
        
        # Print progress every 100 iterations
        if iteration % 100 == 0:
            print(f"Iteration {iteration}, Delta: {delta}")
    
    print(f"Converged after {iteration} iterations")
    print("Final Value Function:")
    print(V)
    
    return V

# Run the value iteration algorithm
if __name__ == "__main__":
    np.set_printoptions(precision=8)
    final_values = gridworld_value_iteration()
