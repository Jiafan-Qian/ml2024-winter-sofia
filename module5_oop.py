#MSCS 2202 module 5 Machine Learning Assignment
# Author: Jiafan Qian
# Created at 02/10/2024

# create a class that initalize the array, add number to array & find number whether in array
class NumbersArray:
    def __init__(self):
        self.numbers = []
        
    def add_number(self, number):
        self.numbers.append(number)
        
    # outputs: "-1" if there were no such X among N read numbers, 
    # or the index (from 1 to N) of this X if the user inputed it before
    def find_number(self, number):
        if number in self.numbers:
            return self.numbers.index(number) + 1 
        else:
            return -1

##################End Class################################
        
#################program running part #####################      
          
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