'''
Hard: (7 points)

3. Write a function that takes an array of integers as input and returns the maximum difference between any two numbers in the array.

Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation of the code you wrote, and include it in the comments of your program.
'''

import numpy as np
import time

numbers = [43, 93, 34, 6, 20, 88, 32]
numbers = np.array(numbers)

def largestDifference(array):

    # analyze time complexity
    start = time.time()

    max_difference = 0

    for i in range(len(array)):
        for j in range(len(array)):
            # compare the left number to the right number moving to the right 
            # AI PROMPT: is there a function that finds the aboslute value in python, for example the distance between -2 and 37
            distance = abs(array[i] - array[j])
            if distance > max_difference:
                max_difference = distance
    
    end = time.time()
    total_time = end - start 

    # print statement
    print(f'The maximum difference between any two numbers in the given array are {max_difference} and the total time to run the function was {total_time}')

    return max_difference

largestDifference(numbers)

# this is O(n^2) notation due to the nessted for loops 
