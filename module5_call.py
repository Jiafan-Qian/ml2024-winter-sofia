#MSCS 2202 module 5 Machine Learning Assignment
# Author: Jiafan Qian
# Created at 02/10/2024

from module5_mod import NumbersArray

# asks the user for input N (positive integer) and reads it
N = int(input("Please enter a positive integer: "))
print(f"Integer you input: {N}")

# asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
print(f"Please provide {N} integer numbers one by one")
numbers = NumbersArray()
for i in range(N):
    number = int(input(f"Please enter number {i+1}: "))
    print("Your input: ", number)
    numbers.add_number(number)

# asks the user for input X (integer)
X = int(input("Please enter an integer: "))

print(numbers.find_number(X))