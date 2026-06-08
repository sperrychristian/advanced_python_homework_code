# O(n^2) sorting algorithims

# sorting algorithims have developed over time and become much faster! 

# searching through a phone book is known as a binary search - a binary search takes a data set, halves it - takes the next chunk or half, then halves it again - until it reaches the search (andy brim)

# if data needs to be stored and searched over and over again - it is absolutely worth the computation time to sort the data first and then search it after it's sorted because we can take advantage of a binary search which is logorithmic and much much faster! 

# bubble sort goes through the entire list comparing two items at a time and swaps them if the item on the left is lower than the one on the right - depending on the data set, it could take many iterations to go through and swap the data as needed

# selection sort - think of it as two pointers are the first two indexes to start. Selection sort takes index one and finds the smallest number in the rest of the data set. Once that has been found, it swaps it and moves onto the next index. So if there was a 9 in index 0 and a 2 in index 7, it would literally swap the 2 to index 0 and the 9 to index 7.

# insertion sort - treats a section like two lists, a sorted portion of the list and an unsorted portion of the list - starts with one item in the sorted portion (index 0) and the rest is unsorted - the algorithim goes through one index at a time and injects from the unsorted portion of the list to the correct index in the sorted list. 

# sort review 
# bubble sort - compares two over and over and again and then swaps the indexes as needed
# selection sort - selects the smalles and then swaps it 
# insertion sort - divides it into two lists and inserts a number from the unsorted side into the sorted side 

#######################################################################

# bubble sort 

list = [3, 1, 4, 1, 5, 9, 2, 6]

for j in range(len(list) - 1):
    for i in range(len(list) - 1):
        # compare two elements and swap if needed 
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
    print(list) # printing list each iteration to visually see what is happening
print(f'bubble sort: {list}')

#######################################################################

# selection sort 

list = [3, 1, 4, 1, 5, 9, 2, 6]

# traverse through all array elements 

for i in range(len(list)):

    # find the minimum elementst in remaining 
    min_index = i 
    for j in range(i + 1, len(list)):
        if list[min_index] > list[j]:
            min_index = j

    # swap the found minimum element with the first element in the list 
    list[i], list[min_index] = list[min_index], list[i]
    print(list) # printing each iteration 

print(f'selection sort: {list}')

#######################################################################

# insertion sort

list = [3, 1, 4, 1, 5, 9, 2, 6]

# traverse through 1 to length of array
for i in range(1, len(list)):
    
    key = list[i]

    # move elements of list[0..i-1], that are greater than key, to one position ahead of their current position 
    j = i - 1
    while j >= 0 and key < list[j]:
        list[j + 1] = list[j]
        j -= 1
    list[j + 1] = key
    print(list) # printing each iteration 

print(f'inertion sort: {list}')

#######################################################################

# recursion sorting is even faster! 

# merge sort 
# O(nlogn) sorting algorithim
# divide list into 2 until all lists are size 1
# then merge lists so they are sorted
# repeat step above until done 

# python program for implimentation of merge sort 
# merges two subarrays of array
# first subbary is [l..m]
# second subbarray is [m + 1 .. r]

def merge(array, l, m, r):
    n1 = m - l + 1  # fix 1: was (m - 1 + 1), should be (m - l + 1) to get correct left subarray size
    n2 = r - m

    # create temporary arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # copy the data to temp arrays L and R
    for i in range(0, n1):
        L[i] = array[l + i]  # fix 2: was array[l + 1], missing the i so it copied the same element every iteration

    for j in range(0, n2):
        R[j] = array[m + 1 + j]

    # merge the temp arrays back into array[l..r]
    i = 0 # initial index of first subarray
    j = 0 # initial index of second subarray
    k = l # fix 3: was k = 1, should be k = l so we write back to the correct position in the original array

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    # copy the remaining elements of L[] if there are any
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    # copy the remaining elementw of R[] if ther are any 
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1
    
# l is for left index and r is for right index of the sub-array of the array to be sorted
def mergeSort(array, l, r):
    if l < r:

        # same as (L + R)//2 but avoids overflow for large L and h
        m = l + (r - l) // 2  # fix 4: was (1 + (r - 1)) // 2, should use l not hardcoded 1

        # sort first and second halves
        mergeSort(array, l, m)
        mergeSort(array, m + 1, r)
        merge(array, l, m, r)

# driver code to test the merge sort functions
array = [12, 11, 13, 5, 6, 7]
print(array)
mergeSort(array, 0, len(array) - 1)
print(f'merge sorted array: {array}')

#######################################################################

# quicksort algorithim
# O(n log n) algorithim 
# uses divide and conquer 
# selects a 'pivot' (a number in the list) and puts everything smaller than the pivot on the left and larger than the pivot on the right 
# repeat steps above recursively until done 

# different from merge sort in the sense that quicksort will sort as it goes down, and doesnt need to work its way back up merging to one big list again

def partition(array, low, high):
    i = (low - 1) # index of a smaller element
    pivot = array[high] # pivot used for start 

    for j in range(low, high):

        # if current element is smaller or equal to pivot 
        if array[j] <= pivot:
            
            # incriment index of smaller element
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return(i + 1)

# the main function that impliments quicksort 
# array[] --> array to be sorted
# low --> starting index
# high --> ending index

# function to do quicksort 

def quickSort(array, low, high):

    if len(array) == 1:
        return array
    if low < high:

        # pi is partitioning index, array[p] is now at the right place
        pi = partition(array, low, high)

        # seperately sort elements before partition and after partition
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

# driver code to test sort quickSort
array = [12, 11, 13, 5, 6, 7]
print(array)
quickSort(array, 0, len(array) - 1)
print(f'quick sorted array: {array}')