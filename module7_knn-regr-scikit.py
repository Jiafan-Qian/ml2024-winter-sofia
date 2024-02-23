#MSCS 2202 module 7 Machine Learning Assignment
# Author: Jiafan Qian
# Created at 02/23/2024

import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

# asks the user for input N (positive integer) and reads it
N = int(input("Please input N (positive integer): "))
print(f"value of N: {N}")

# Then the program asks the user for input k (positive integer) and reads it.
k = int(input("Please input k (positive integer): "))
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

    # #asks the user for input X 
    X = float(input("Please input X : "))

    #outputs: the result (Y) of k-NN Regression
    # Reshape training data for scikit-learn fit function
    trainingData = np.array(trainingData)
    XTrain= trainingData[:, 0].reshape(-1, 1)  
    YTrain = trainingData[:, 1]
    knnRegressionModel = KNeighborsRegressor(n_neighbors=k)
    knnRegressionModel.fit(XTrain, YTrain)
    YPredict = knnRegressionModel.predict(np.array([[X]]))

    #outputs: r2, coefficient of determination.
    YPredictUsingTrainingData = knnRegressionModel.predict(XTrain)
    r2 = r2_score(YTrain, YPredictUsingTrainingData)

    print(f"result of k-NN regression with Euclidean distances for X = {X} is: {YPredict[0]}")
    print(f"Coefficient of determination (R^2): {r2}")
