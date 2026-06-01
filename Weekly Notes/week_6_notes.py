# big oh notation 
# used when we're comparing algorithims and talking about efficiency (runtime)
# 'this one is more efficient because it uses the big o notation of x'
# 'n' refers to the number of inputs - how long does it take the algorithim to generate the outputs. 
# a list might have 1000 items. 

# big oh notation is the most popular way to measure algorithim efficiency because it refers to worst case runtime 

# constant time - O(c) - asking what is the first item in the list and how long does it take to access it 
# linear time - O(n) - goes through the list one item at a time and how long does it take 
# quadratic time - O(n^2) - in an algorith, measuring the time to go through two nested for loops, O(n^3) would just be 3 nested for loops
# logorithimic time - ?

# examples 
import time # the time library is a great way to measure how long it takes for a program to run!
list = [1, 3, 4, 5, 6, 7, 9, 44, 2, 23, 0]

# O(n) example - we're looping through the list of 11 items, 11 operations are being performed
for i in list:
    print(i)

# O(n^2) operation timing it! 

start = time.time() # time.time() will give a timestamp of when our runtime started

for i in range(1000):
    for j in range(1000):
        print(i * j)

end = time.time()
print('runtime (seconds):', end - start)

# # example of O(n^4) - takes much longer! For algorithim analysis we need to keep track of the coefficient. The best way to do this is just to keep nested for loops to a minimum! Sometimes it cannot be avoided.
 
# start = time.time() # time.time() will give a timestamp of when our runtime started

# for i in range(1000):
#     for j in range(1000):
#         for k in range(1000):
#             for m in range(1000):
#                 print(i * j * k * m, end=" ")

# end = time.time()
# print('runtime (seconds):', start - end)

# another O(n^2) example - this is still an order n squared operation because it it just two nested for loops
list_2 = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]

total = 0
count = 0 

for row in list_2:
    for item in row:
        total += item
        count += 1

print('Average:', total/count)

# sorting algorithms are are a great way to perform algorithim analysis - this is an n squared big o notation

# bubble sort
bubble_list = [3, 1, 4, 5, 6, 7, 9, 44, 2, 23, 0]

for j in range(len(bubble_list) - 1):
    for i in range(len(bubble_list) - 1):
    # compare elements and swap if element 1 is greater
        if bubble_list[i] > bubble_list[i + 1]:
            # python has great syntax for switching the contents do to how the interpreter is set up 
            bubble_list[i], bubble_list[i +1] = bubble_list[i + 1], bubble_list[i]

print('bubble sorted list:', bubble_list)

# recursion vs iteration 

# iteration is looping through a problem - think for loop - there are many reasons we would need to do this.
# another concept is recursion - recursion can also handle a repetative process

# recursion example - print numbers 1 - 1000

# iteration loop example 
nums = [4, 9, 5, 2, 6, 0]

def printList(list):
    for i in range(len(list)):
        print(list[i])
    return 

printList(nums)

# print using recursion 
# each time we come into this function, we call this function again and it starts over 
# just like we can get into an infinate loop, we also can have infinate recursion - we add a base case that tells the recursion to stop 
def printRecursion(list, start):
    if start == len(list):
        return 
    
    print(list[start])
    printRecursion(list, start + 1)

    return 

printRecursion(nums, 0)

# anything we can do iterively, we can do recursively 
# most problems we come across, the correct way is to use iteration 

# there are problems that exist that are recursive by nature
# the logic to handle the superset of the problem is the logic to handle the subset of the problem 

# the four parts of the recursive function 
# 1 - base case - the logic that handles the stopping of the recursion 
# 2 - recursive call 
# 3 - logic
# 4 - return 

# recursion - returning a function call 
# recursion is simply when a function calls itself 
# recusion and iteration are like brother and sister - both great tools but better used in different scenarios

# example - sum numbers 1 - n
def sumNumbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i

    return sum 

print(sumNumbers(5))


# doing the same thing recursively 

def sumNumbersRecursive(n):
    if n == 1:
        return n # this is our base case 
    
    return n + sumNumbersRecursive(n - 1) # this will continue to call the function recursively 5 + 4 + 3 + 2 + 1

print(sumNumbersRecursive(5))

# recursion - factorial example 
# a factorial is factorial by nature - aka much easier to use recursion vs iteration 

# iterative 
def multiplyNumbers(n):
    total = 1
    for i in range(1, n+1):
        total *= i

    return total 

print(multiplyNumbers(5))

# recursive
def multiplyNumbersRecursive(n):
    if n == 1: # base case 
        return n 
    
    return n * multiplyNumbersRecursive(n - 1)

print(multiplyNumbersRecursive(5))

# recursion fibonacci example - recursive by nature 
# each term in the sequence is a calculation of the previous 2 numbers 
# 0 and 1 are by rule the first two terms 

# iterative 
def fibiter(n):
    f1 = 1 
    f2 = 1
    tmp = 1
    for i in range(1, int(n)-1):
        tmp = f1 + f2
        f1 = f2
        f2 = tmp

    return f2
    
print(fibiter(10))

# recursion 
def fibiterRecursion(n):
    if n < 2:
        return n
    return fibiterRecursion(n - 1) + fibiterRecursion(n - 2)

print(fibiterRecursion(10))

# recursion - towers of hanoi example - recursive by nature
# recursions are when a function can call itself 



