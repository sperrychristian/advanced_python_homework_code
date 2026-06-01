'''
Medium: (5 points)

2. Given an array of integers, write a function that finds the second largest number in the array.

Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation of the code you wrote, and include it in the comments of your program.
'''

import numpy as np
import time

numbers = [43, 93, 34, 6, 20, 88, 32]
numbers = np.array(numbers)

def secondLargestNumberFinder(array):
    # time complexity 
    start = time.time()

    for i in range(len(array) - 1): 
        # a nested for loop to compare the numbers set up the same way the content vids set up the bubble sort problem 
        for j in range(len(array) - 1):
            # compare the left number to the right number moving to the right 
            if array[j] > array[j + 1]:
                # swap the numbers to sort them 
                array[j], array[j + 1] = array[j + 1], array[j]
    
    # now that we have a sorted list, reverse the order and return index 1 
    # AI PROMPT: remind me the syntax to reverse a list in python, confirm that this will also apply to numpy arrays
    list_reversed = array[::-1]

    end = time.time()
    total_time = end - start 

    second_highest_number = list_reversed[1]

    print(f'The second highest number in the array is {second_highest_number} and the total time to run is {total_time}')
    # return the result and the total time 
    return second_highest_number, total_time

secondLargestNumberFinder(numbers)

# this algorithim uses O(n^2) quadratic notation because of the nested for loop


