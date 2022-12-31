import random

# Define the function to be optimized
def objective_function(x):
    return x**2 + x - 6

# Set the initial solution and the tabu list
solution = random.uniform(-10, 10)
tabu_list = []

# Set the parameters for the tabu search
max_iterations = 1000
max_no_improvement = 100

# Initialize the best solution found so far
best_solution = solution
best_value = objective_function(solution)

# Start the tabu search
for i in range(max_iterations):
    # Generate a list of possible moves
    moves = []
    for j in range(-10, 11):
        if j != 0 and j not in tabu_list:
            moves.append(j)

    # Select the best move from the list of possible moves
    best_move = 0
    best_move_value = float('inf')
    for move in moves:
        new_solution = solution + move
        new_value = objective_function(new_solution)
        if new_value < best_move_value:
            best_move = move
            best_move_value = new_value

    # Update the solution and the tabu list
    solution += best_move
    tabu_list.append(best_move)
    if len(tabu_list) > max_no_improvement:
        tabu_list.pop(0)

    # Update the best solution found so far
    if best_move_value < best_value:
        best_solution = solution
        best_value = best_move_value

# Print the best solution found
print("Best solution:", best_solution)
print("Best value:", best_value)