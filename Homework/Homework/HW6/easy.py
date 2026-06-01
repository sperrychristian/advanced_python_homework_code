''' 
Easy: (3 points)

1. Given an array of integers, write a function to calculate the sum of all elements in the array.

Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation of the code you wrote, and include it in the comments of your program.
'''

import numpy as np
import time 

# taking a list of integers and converting them into an array
numbers = [43, 93, 34, 6, 20, 88, 32]
numbers = np.array(numbers)

def calculateSum(array):
    # calculating the time complexity within the function itself 
    start = time.time()

    # initilize ta sum
    sum = 0

    # add each number in the array to the sum
    for number in array:
        sum += number
    
    end = time.time()

    # calculate the total time 
    total_time = end - start 

    # function returns sum of all integers and total time
    print(f'sum of all numbers in array: {sum}, total time: {total_time}')
    return

# print statement is written into my function so I just call it here 
calculateSum(numbers)


# the big o notation  is O(n) because it's linear, going through the array and adding together its contents
# NO AI USED TO SOLVE THIS PROBLEM 


    