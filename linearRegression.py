# Number of observations
# y = mx + c
n = int(input("Enter number of observations: "))

x = []
y = []

print("Enter X values:")
for i in range(n):
    x.append(int(input(f"Value at X[{i+1}] = ")))

print("Enter Y values:")
for i in range(n):
    y.append(int(input(f"Value at Y[{i+1}] = ")))


sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(x[i] * y[i] for i in range(n))
sum_x2 = sum(xi ** 2 for xi in x)

print(sum_x)
print(sum_y)
print(sum_xy)
print(sum_x2)

# slope (m)
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2) 

# intercept (c)
c = (sum_y - m * sum_x) / n

print("\nLinear Regression Equation:")
print(f"Y = {m:.4f}X + {c:.4f}")

x_pred = float(input("\nEnter X value to predict Y: "))
y_pred = m * x_pred + c

print(f"Predicted Y = {y_pred:.4f}")

sse = 0

for i in range(n):
    y_hat = m * x[i] + c
    sse += (y[i] - y_hat) ** 2

print(f"SSE = {sse:.4f}")