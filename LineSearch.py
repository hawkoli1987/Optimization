def line_search(objective_function, x, gradient, search_direction, step_size=1.0, c1=0.1, c2=0.9):
    # Initialize the step size
    alpha = step_size

    # Compute the initial objective function value and gradient
    f0 = objective_function(x)
    grad0 = gradient(x)

    # Compute the initial directional derivative
    grad0_dot_dir = np.dot(grad0, search_direction)

    # Check the strong Wolfe conditions to ensure that we are making sufficient progress
    while True:
        # Compute the new point along the search direction
        x_new = x + alpha * search_direction

        # Compute the objective function value at the new point
        f_new = objective_function(x_new)

        # Check the first Wolfe condition (sufficient decrease)
        if f_new <= f0 + c1 * alpha * grad0_dot_dir:
            # Compute the gradient at the new point
            grad_new = gradient(x_new)

            # Check the second Wolfe condition (curvature condition)
            if np.dot(grad_new, search_direction) >= c2 * grad0_dot_dir:
                return alpha, x_new, f_new, grad_new

        # If the conditions are not met, reduce the step size and try again
        alpha = alpha * 0.5