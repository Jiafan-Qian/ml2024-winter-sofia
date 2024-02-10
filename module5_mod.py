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