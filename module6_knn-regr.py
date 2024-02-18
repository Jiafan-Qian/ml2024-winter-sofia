#MSCS 2202 module 6 Machine Learning Assignment
# Author: Jiafan Qian
# Created at 02/17/2024

def k_nn_regression(trainingData, k, X):
    # calculate the Euclidean distances
    distances = np.sqrt((trainingData[:, 0] - X) ** 2)
    # get the the indices for k smallest distances
    nearestKValueIndices = np.argsort(distances)[:k]
    # calculate predict y value
    yPrediction = np.mean(trainingData[nearestKValueIndices])
    return yPrediction

import numpy as np

# asks the user for input N (positive integer) and reads it
N = int(input("Please input N (positive integer): "))
print(f"value of N: {N}")

# Then the program asks the user for input k (positive integer) and reads it.
k = int(input("Please input k (positive number): "))
print(f"value of k: {k}")

# print error message if k > N
if k > N:
    print("k should be smaller than N")
else:
    #asks the user to provide N (x, y) points (one by one) and reads all of them: 
    # first: x value, then: y value for every point one by one. 
    # X and Y are the real numbers.

    # initialize a 2-D array
    trainingData = np.zeros((N, 2))

    for i in range(N):
        x = float(input(f"Enter value x for point {i + 1}: "))
        y = float(input(f"Enter value y for point {i + 1}: "))
        print(f"point {i + 1} is: ({x}, {y})")
        trainingData[i] = [x, y]

    #asks the user for input X 
    X = float(input("Please input X : "))
    
    #outputs: the result (Y) of k-NN Regression
    YPredict = k_nn_regression(trainingData, k, X)
    print(f"result of k-NN regression with Euclidean distances for X = {X} is: {YPredict}")
