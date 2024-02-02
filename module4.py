#MSCS 2202 module 4 Machine Learning Assignment
# Author: Jiafan Qian
# Created at 02/01/2024

# note that the following code requires user to input integers
# decimal numbers or negative numbers may cause errors

# asks the user for input N (positive integer) and reads it
N = int(input("Please enter a positive integer: "))
print(f"Integer you input: {N}")

# asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
print(f"Please provide {N} integer numbers one by one")
numbers = []
for i in range(N):
    number = int(input(f"Please enter number {i+1}: "))
    print("Your input: ", number)
    numbers.append(number)

# asks the user for input X (integer)
X = int(input("Please enter an integer: "))

# outputs: "-1" if there were no such X among N read numbers, 
# or the index (from 1 to N) of this X if the user inputed it before
if X in numbers:
    print(numbers.index(X) + 1)
else:
    print("-1")