import numpy as np

def lagrangian_multipliers(obj, constraints, x0, l0):
    """
    Solve an optimization problem using the method of Lagrange multipliers.
    
    Parameters
    ----------
    obj : callable
        The objective function to minimize.
    constraints : list of callable
        The constraints of the optimization problem.
    x0 : ndarray
        The initial guess for the optimization variables.
    l0 : ndarray
        The initial guess for the Lagrange multipliers.
    
    Returns
    -------
    x : ndarray
        The optimal values of the optimization variables.
    l : ndarray
        The optimal values of the Lagrange multipliers.
    """
    def lagrangian(x, l):
        return obj(x) + np.sum(l[i] * constraints[i](x) for i in range(len(constraints)))
    
    def grad_lagrangian(x, l):
        return np.array([
            obj.gradient(x) + np.sum(l[i] * constraints[i].gradient(x) for i in range(len(constraints))),
            [constraints[i](x) for i in range(len(constraints))]
        ])
    
    def solve_kkt(x, l):
        return grad_lagrangian(x, l)
    
    x = x0
    l = l0
    kkt_tol = 1e-6
    
    while True:
        kkt_residual = solve_kkt(x, l)
        kkt_norm = np.linalg.norm(kkt_residual)
        if kkt_norm < kkt_tol:
            break
        x, l = x - kkt_residual[0], l - kkt_residual[1]
    
    return x, l