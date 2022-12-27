import numpy as np

# Define the function to be optimized
def objective_function(x):
    return (x[0] - 2)**2 + (x[1] - 3)**2

# Define the gradient of the objective function
def gradient(x):
    return np.array([2 * (x[0] - 2), 2 * (x[1] - 3)])

# Define the Hessian of the objective function
def Hessian(x):
    return np.array([[2, 0], [0, 2]])

# Set the initial solution and the Levenberg-Marquardt parameters
x = np.array([0, 0])
lambda_ = 0.1
tolerance = 1e-6

# Perform the Levenberg-Marquardt optimization
while True:
    # Compute the Jacobian and the residuals
    J = gradient(x)
    r = objective_function(x)

    # Compute the Hessian and the gradient of the residuals
    H = Hessian(x) + lambda_ * np.eye(2)
    g = J.T @ r

    # Check for convergence
    if np.linalg.norm(g) < tolerance:
        break

    # Compute the update
    dx = np.linalg.solve(H, -g)
    x += dx

    # Update the value of lambda
    if r.dot(r) > (r + J @ dx).dot(r + J @ dx):
        lambda_ *= 10
    else:
        lambda_ /= 10

# Print the solution
print("Solution:", x)