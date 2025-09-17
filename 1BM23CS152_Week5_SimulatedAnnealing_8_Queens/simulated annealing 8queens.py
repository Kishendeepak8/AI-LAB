import random
import math

# Function to compute cost: number of attacking pairs
def compute_cost(state):
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

# Generate a random neighbor by moving one queen
def get_neighbor(state):
    n = len(state)
    new_state = state.copy()
    col = random.randint(0, n-1)         # choose a column
    new_row = random.randint(0, n-1)     # new row
    while new_row == new_state[col]:     # ensure change
        new_row = random.randint(0, n-1)
    new_state[col] = new_row
    return new_state

# Simulated Annealing Algorithm
def simulated_annealing(n=8, T=1000, alpha=0.95, max_iter=100000):
    # Step 1: Initial random state
    current = [random.randint(0, n-1) for _ in range(n)]
    current_cost = compute_cost(current)

    for step in range(max_iter):
        if current_cost == 0:
            return current  # solution found

        # Step 2: Generate neighbor
        neighbor = get_neighbor(current)
        neighbor_cost = compute_cost(neighbor)

        # Step 3: Difference in cost
        deltaE = current_cost - neighbor_cost

        # Step 4: Acceptance criteria
        if deltaE > 0:  # better state
            current, current_cost = neighbor, neighbor_cost
        else:
            # accept worse state with probability
            prob = math.exp(deltaE / T)
            if random.random() < prob:
                current, current_cost = neighbor, neighbor_cost

        # Step 5: Decrease temperature
        T = alpha * T
        if T <= 0.0001:
            break

    return current  # return best found solution

# Helper to print board
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

# Run the algorithm
solution = simulated_annealing()
print("Final Solution (State Representation):", solution)
print("Final Cost:", compute_cost(solution))
print("Board:")
print_board(solution)
