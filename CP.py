from ortools.sat.python import cp_model

# Create the model
model = cp_model.CpModel()

# Define the variables
x = model.NewIntVar(0, 10, "x")
y = model.NewIntVar(0, 10, "y")

# Define the constraints
model.Add(x + y <= 10)
model.Add(2 * x + y <= 15)

# Define the objective function
model.Maximize(x + 2 * y)

# Solve the problem
solver = cp_model.CpSolver()
status = solver.Solve(model)

# Print the solution
if status == cp_model.OPTIMAL:
    print("Solution:")
    print("x =", solver.Value(x))
    print("y =", solver.Value(y))
else:
    print("No solution found.")