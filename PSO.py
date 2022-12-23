import numpy as np

# Define the function to optimize
def f(x):
  return x**2 + 10*np.sin(x)

# Set the number of particles
num_particles = 50

# Set the maximum number of iterations
max_iterations = 100

# Set the convergence tolerance
tolerance = 1e-6

# Set the initial positions of the particles
particle_positions = np.random.uniform(-10, 10, (num_particles, 1))

# Set the initial velocities of the particles
particle_velocities = np.zeros((num_particles, 1))

# Set the initial personal best positions of the particles
personal_best_positions = particle_positions.copy()

# Set the initial global best position
global_best_position = np.min(personal_best_positions, axis=0)

# Set the acceleration constants
c1 = 2
c2 = 2

# Set the inertia weight
inertia_weight = 0.8

# Iterate until the maximum number of iterations is reached
for i in range(max_iterations):
  
  # Update the velocities of the particles
  particle_velocities = inertia_weight * particle_velocities + c1 * np.random.uniform(0, 1, (num_particles, 1)) * (personal_best_positions - particle_positions) + c2 * np.random.uniform(0, 1, (num_particles, 1)) * (global_best_position - particle_positions)
  
  # Update the positions of the particles
  particle_positions = particle_positions + particle_velocities
  
  # Update the personal best positions of the particles
  personal_best_positions = np.where(f(particle_positions) < f(personal_best_positions), particle_positions, personal_best_positions)
  
  # Update the global best position
  global_best_position = np.min(personal_best_positions, axis=0)
  
  # Check if the solution has converged
  if np.abs(global_best_position - np.min(particle_positions, axis=0)) < tolerance:
    break

# Print the solution
print(global_best_position)