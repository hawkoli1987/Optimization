import random

def simulated_annealing(start_temp, end_temp, num_iterations):
    # Initialize the current solution to a random point
    current_solution = random.uniform(-10, 10)
    best_solution = current_solution
    
    # Set the current temperature and the cooling rate
    temperature = start_temp
    cooling_rate = (start_temp - end_temp) / num_iterations
    
    # Iterate over the number of iterations
    for i in range(num_iterations):
        # Generate a random neighbor
        new_solution = random.uniform(-10, 10)
        
        # Calculate the acceptance probability
        acceptance_probability = min(1, pow(2.71828, -abs(new_solution - current_solution) / temperature))
        
        # Determine whether to accept the new solution
        if acceptance_probability > random.random():
            current_solution = new_solution
        
        # Update the best solution if necessary
        if abs(current_solution) < abs(best_solution):
            best_solution = current_solution
        
        # Cool the temperature
        temperature -= cooling_rate
    
    # Return the best solution
    return best_solution

print(simulated_annealing(100, 0, 10000))