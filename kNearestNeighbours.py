import matplotlib.pyplot as plt

# Number of observations
n = int(input("Enter number of observations: "))

# Number of features
f = int(input("Enter number of features: "))

# Feature names
feature_names = []

for i in range(f):
    name = input(f"Enter name of Feature {i+1}: ")
    feature_names.append(name)

# Training data
data = []

for i in range(n):
    print(f"\nObservation {i+1}")

    row = []

    for feature in feature_names:
        value = float(input(f"Enter {feature}: "))
        row.append(value)

    label = input("Enter Class Label: ")
    row.append(label)

    data.append(row)

# Test Data
print("\nEnter values for prediction:")

test_point = []

for feature in feature_names:
    value = float(input(f"Enter {feature}: "))
    test_point.append(value)

# K Value
k = int(input("Enter value of K: "))

# Distance Calculation
distances = []

for row in data:

    distance = 0

    for j in range(f):
        distance += (row[j] - test_point[j]) ** 2

    distance = distance ** 0.5

    distances.append((distance, row[-1]))

# Sort Distances
distances.sort()

# K Nearest Neighbors
neighbors = distances[:k]

# Voting
votes = {}

for distance, label in neighbors:
    if label in votes:
        votes[label] += 1
    else:
        votes[label] = 1

prediction = max(votes, key=votes.get)

print("\nNearest Neighbors:")
for distance, label in neighbors:
    print(f"Distance = {distance:.4f}, Class = {label}")

print(f"\nPredicted Class = {prediction}")

# Scatter Plot (only if there are at least 2 features)
if f >= 2:

    x_values = []
    y_values = []

    for row in data:
        x_values.append(row[0])
        y_values.append(row[1])

    plt.scatter(x_values, y_values)
    plt.scatter(test_point[0], test_point[1], marker="X", s=100)

    plt.xlabel(feature_names[0])
    plt.ylabel(feature_names[1])
    plt.title("KNN Scatter Plot")

    plt.show()

else:
    print("Scatter plot requires at least 2 features.")