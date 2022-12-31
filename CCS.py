def ccs(objective_function, x, max_iter=100, tol=1e-6):
    # Initialize the number of iterations
    iter = 0

    # Initialize the change in the objective function value
    delta = float('inf')

    # Iterate until the maximum number of iterations has been reached or the change in the objective function is below the tolerance
    while iter < max_iter and delta > tol:
        # Store the current objective function value
        f_old = objective_function(x)

        # Iterate over the variables
        for i in range(len(x)):
            # Save the current value of the variable
            x_old = x[i]

            # Perform a one-dimensional optimization to find the optimal value of the variable
            x[i] = optimize.minimize_scalar(objective_function, bounds=(x_old - 1, x_old + 1)).x

            # Compute the change in the objective function value
            delta = np.abs(f_old - objective_function(x))

        # Increment the iteration counter
        iter += 1

    # Return the optimal values of the variables
    return x