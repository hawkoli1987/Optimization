import numpy as np

# Define the function to optimize
def f(x):
  return x**2 + 10*np.sin(x)

# Define the derivative of the function
def f_prime(x):
  return 2*x + 10*np.cos(x)

# Set the initial guess for the solution
x = 3

# Set the maximum number of iterations
max_iterations = 10

# Set the convergence tolerance
tolerance = 1e-6

# Iterate until the maximum number of iterations is reached
for i in range(max_iterations):
  
  # Calculate the next estimate using the Newton-Gauss method
  x_new = x - f_prime(x) * (x - x_prev) / (f_prime(x) - f_prime(x_prev))
  
  # Check if the solution has converged
  if abs(x_new - x) < tolerance:
    break
  
  # Update the current and previous estimates
  x_prev = x
  x = x_new

# Print the solution
print(x)