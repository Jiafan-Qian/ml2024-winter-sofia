#MSCS 2202 module 8 Machine Learning Assignment
# Author: Jiafan Qian
# Created at 03/02/2024

import numpy as np
from sklearn.metrics import precision_score, recall_score

# asks the user for input N (positive integer) and reads it
N = int(input("Please input N (positive integer): "))
print(f"value of N: {N}")

#Then asks the user to provide N (x, y) points (one by one) and reads all of them: 
# first: x value, then: y value for every point one by one. 
# X is treated as the ground truth (correct) class label and Y is treated as the predicted class. 
# Both X and Y are either 0 or 1.

X = np.zeros(N)
Y = np.zeros(N)

for i in range(N):
    x = int(input(f"Enter value x for point {i + 1}: "))
    y = int(input(f"Enter value y for point {i + 1}: "))
    X[i] = x
    Y[i] = y

# outputs: the Precision and Recall based on the inputs.
precision = precision_score(X, Y)
recall = recall_score(X, Y)

print(f"Precision is: {precision}")
print(f"Recall is: {recall}")