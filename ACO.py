import random

def ant_colony(num_ants, num_iterations, num_cities, distances, decay, alpha=1, beta=1):
    # Initialize the pheromone matrix
    pheromones = [[1 / num_cities for j in range(num_cities)] for i in range(num_cities)]
    
    # Initialize the best path to an empty list
    best_path = []
    best_distance = float("inf")
    
    # Iterate over the number of iterations
    for i in range(num_iterations):
        # Initialize the paths and distances for each ant
        paths = []
        distances = []
        
        # Have each ant search for a path
        for j in range(num_ants):
            path = [random.randint(0, num_cities - 1)]
            visited = set(path)
            distance = 0
            for k in range(num_cities - 1):
                # Calculate the transition probabilities for each city
                probs = [0 for l in range(num_cities)]
                for l in range(num_cities):
                    if l not in visited:
                        prob = (pheromones[path[-1]][l] ** alpha) * ((1 / distances[path[-1]][l]) ** beta)
                        probs[l] = prob / sum(probs)
                
                # Select the next city based on the transition probabilities
                next_city = random.choices(range(num_cities), weights=probs)[0]
                path.append(next_city)
                visited.add(next_city)
                distance += distances[path[-2]][path[-1]]
            
            # Add the path and distance for this ant to the list
            paths.append(path)
            distances.append(distance)
        
        # Update the pheromone matrix
        for j in range(num_cities):
            for k in range(num_cities):
                pheromones[j][k] *= decay
                for path, distance in zip(paths, distances):
                    if k in path and path.index(k) > 0:
                        pheromones[j][k] += 1 / distance
        
        # Update the best path and distance if necessary
        for path, distance in zip(paths, distances):
            if distance < best_distance:
                best_path = path
                best_distance = distance
    
    # Return the best path
    return best_path

print(ant_colony(10, 100, 10, [[0, 2, 3, 1, 5, 4, 7, 8, 9, 6], [2, 0, 1, 4, 3, 6, 5, 8, 9, 7], [3, 1, 0, 5, 4, 7, 6, 9, 8, 2], [1, 4, 5, 0, 7, 2, 8, 3, 6, 9