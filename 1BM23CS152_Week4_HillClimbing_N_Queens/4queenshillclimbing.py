import random

# Function to compute cost: number of attacking pairs
def compute_cost(state):
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

# Generate all neighbors (by moving one queen in its column)
def get_neighbors(state):
    neighbors = []
    n = len(state)
    for col in range(n):
        for row in range(n):
            if row != state[col]:
                new_state = state.copy()
                new_state[col] = row
                neighbors.append(new_state)
    return neighbors

# Hill Climbing Algorithm
def hill_climbing(n=4):
    # Step 1: Random initial state
    current = [random.randint(0, n-1) for _ in range(n)]
    current_cost = compute_cost(current)

    print("Initial State:", current, "Cost:", current_cost)
    print_board(current)

    while True:
        neighbors = get_neighbors(current)
        # Evaluate neighbors
        best_neighbor = min(neighbors, key=lambda x: compute_cost(x))
        best_cost = compute_cost(best_neighbor)

        # Print move
        print("Best Neighbor:", best_neighbor, "Cost:", best_cost)

        # Step 2: If no improvement, stop
        if best_cost >= current_cost:
            return current, current_cost

        # Step 3: Move to better neighbor
        current, current_cost = best_neighbor, best_cost
        print_board(current)

        # Step 4: Goal check
        if current_cost == 0:
            return current, current_cost

# Print board helper
def print_board(state):
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)
    print("\n")

# Run Hill Climbing for 4-Queens
solution, cost = hill_climbing(4)
print("Final Solution:", solution, "Cost:", cost)
