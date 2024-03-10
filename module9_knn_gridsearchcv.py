#MSCS 2202 module 9 Machine Learning Assignment
# Author: Jiafan Qian
# Created at 03/09/2024

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# asks the user to provide N (x, y) pairs (one by one) 
# and reads all of them: first: x value, then: y value for every pair one by one. 
# X is treated as the input feature and Y is treated as the class label. 
# X is a real number, Y is a non-negative integer.
def createPairs(n):
    pairs = np.zeros((n, 2))
    for i in range(N):
        x = float(input(f"Enter value x for point {i + 1}: "))
        y = int(input(f"Enter value y for point {i + 1}: "))
    pairs[i] = [x, y]
    return pairs


# asks the user for input N (positive integer) and reads it
N = int(input("Please input N (positive integer): "))
print(f"value of N: {N}")
# use createPairs to create the training set TrainS = {(x, y)_i}, i = 1..N.
TrainS = createPairs(N)

# asks the user for input M (positive integer) and reads it.
M = int(input("Please input N (positive integer): "))
print(f"value of N: {M}")
# use createPairs to create test set TestS = {(x, y)_i}, i = 1..M.
TestS = createPairs(M)

# the program outputs: the best k for the kNN Classification method 
# and the corresponding test accuracy. 
# kNN Classifier should be trained on pairs from TrainS, 
# tested on x values from TestS and compared with y values from TestS.

# find the best k
# initialize the best k and accuracy
bestK = 0
bestAccuracy = 0
# prepare data that used in knn classification model
xTrain = TrainS[:, 0].reshape(-1, 1)
yTrain = TrainS[:, 1]
xTest = TestS[:, 0].reshape(-1, 1)
yTest = TestS[:, 1]

# Note: you can try the following range of k: 1 <= k <= 10.
for k in range(1, 11):
    # find the model and accuracy for current k
    knnClassification = KNeighborsClassifier(n_neighbors=k)
    knnClassification.fit(xTrain, yTrain)
    prediction = knnClassification.predict(xTest)
    accuracy = accuracy_score(yTest, prediction)
    # update the best accuracy and best k value
    # if the model with current k has a better accuracy
    if accuracy > bestAccuracy:
        bestAccuracy = accuracy
        bestK = k

print(f"The best k is :{bestK}")
print(f"The correspondng test accuracy is: {bestAccuracy}.")