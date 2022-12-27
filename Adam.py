def adam(params, grads, m, v, t, learning_rate=0.001, beta1=0.9, beta2=0.999, eps=1e-8):
    # Iterate over the parameters
    for param, grad in zip(params, grads):
        # Update the moment estimates
        m[param] = beta1 * m[param] + (1 - beta1) * grad
        v[param] = beta2 * v[param] + (1 - beta2) * grad**2

        # Correct the moment estimates
        m_hat = m[param] / (1 - beta1**t)
        v_hat = v[param] / (1 - beta2**t)

        # Update the parameter
        param -= learning_rate * m_hat / (np.sqrt(v_hat) + eps)