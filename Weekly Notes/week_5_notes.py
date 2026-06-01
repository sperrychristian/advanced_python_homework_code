# list comprehension
# list comprehension is a nice way to add values to a list in one line! 
# similiar to augmented operator

# reminder on how to add  values to a list using a for loop 
list = []
for i in range(100):
    list.append(i)

print(list)

# doing the same thing with list comprehension 
# (adding the variable to the front of the list tells the list to execute the for loop and add the values to the list)
list_2 = [i for i in range(50)]

print(list_2)

# updating each value in list comprehension 
list_2 = [str(i) for i in range(25)]

print(list_2)

# # real world list comprehension example 
# file = open('/workspaces/advanced_python_homework_code/Weekly Notes/programming_activity.txt')
# lines = file.readlines() # this reads all the lines of the file into a list called lines, but they are still strings! 
# prices = [float(i) for i in lines] # this uses list comprehension to add the list of stock prices into a list that is 100% floats instead of strings

# list comprehensions are really nice for reading in data and converting it to different types of data


# two dimension lists 
# two dimensional lists just store lists within lists, spreadsheets are an example of a two dimensional list. (10 x 10 list)

table = []
for i in range(10):
    table.append([]) 

print(table) # list of 10 lists
for i in range(10):
    for j in range(10):
        table[i].append(i * j)

for row in table:
    print(row)

# nested for loops and two dimensional lists are like brothers and sisters, you need a multidimensional loop to handle a multi dimensional list
for i in range(10):
    for j in range(10):
        print(table[i][j], end =' ') # i goes into the first index or first list, j goes into that list and prints out the index of the nested list 
    print('')

# list of student scores 

christian =[100, 99, 101]
madi = [100, 100, 100]
teton = [50, 34, 93]

student_scores = [christian, madi, teton]

for student in student_scores:
    for score in student:
        print(score, end=' ')
    print()


# queus and stacks 

# python lists should contain homogenious data 
# lists and arrays contain a sequence of data of the same data type 

# a que stores data in fifo format, meaning first in, first out. The data that goes in first is also the data that goes out first. 
# think of a line in the real world, this works the same way. 

# a stack on the other hand is lifo, last in first out. When the data goes in, it's the first thing to come out. 
# a stack of pancakes in the real world would be lifo. 

# queues and stacks in python 
# to use a que in python, we would use a normal list but end up accessing it a little bit differently 

queue = []

queue.append('a')
queue.append('b')
queue.append('c')

print('initial que')
print(queue)

# the .pop() function allows us to specify the index we want to pop off. Normally, it pops the last item out of the list behaving like a stack. In this case we are telling it to pop out index 0, which would be the oldest item in the queue

queue.pop(0)
print(queue)
queue.pop(0)
print(queue)
queue.pop(0)
print(queue)

# stacks python examples (lifo)
# a python list also works great as a stack

stack = []
stack.append('as')
stack.append('bs')
stack.append('cs')
print(stack)

# calling pop with no arguments just takes the last item in the list and returns that object
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

# queues in practice - trading example 
# choosing a queue as a data structure can make for very efficient data structures
# we can create a priority queue that bumps it up in the line 

# numpy arrays
# libary in python used for all types of numeric data
# tons of functions for math and statistics
# heavily used for storing data because they use much less memory and they're much faster than the native python list

# creat a list of 4 floats
scores = [33.4, 43.7, 99.5, 2.45]
print(scores)

# convert to a numpy arrray 
import numpy
hw_scores = numpy.array(scores)
print(hw_scores) # the numpy array prints with spaces instead of commas

# python uses an intrepeter, it goes line by line and converts python code to machine code. In that process, python code is converted to C code. Since python is already converting to C, numpy stores the data as a C datatype. For that reason, it's much faster for the python interpreter to process the data.

# we should use numpy as a standard. Get used to using numpy and other c datatypes because that is how they're used professionally 

# initilize a numpy array the size of 10
np1 = numpy.zeros(100) # the zeros function is built in literally just for the functionality of initilizing an array. This is one of those tricks used for efficiency. Memory now knows that this array will hold 100 number data types
print(np1)

