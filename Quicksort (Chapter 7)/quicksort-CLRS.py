'''
Sudo Code from Introduction to Algorithms, CLRS, 4th Edition

QUICKSORT(A, p, r)

    if p < r
        // Partition the subarray around the pivot, which ends up in A[q] 
        q = PARTITION(A, p, r) 
        QUICKSORT(A, p, q - 1)  // recursively sort the low side
        QUICKSORT(A, q + 1, r)  // recursively sort the high side

PARTITION(A, p, r)

    x = A[r]                            // the pivot
    i = p - 1                           // highest index into the low side
    for j = p to r - 1                  // process each element other than the pivot 
        if A[j] <= x                    // does this element belong on the low side 
            i = i + 1                   // index of the new slot in the low side
            exchange A[i] with A[j]     // put this element there
    exchange A[i + 1] with A[r]         // pivot goes just to the right of the low side
    return i + 1                        // new index of the pivot

'''

import random
import timeit

def exchange (array, i, j):
    tempi = array[i]
    tempj = array[j]
    array[i] = tempj
    array[j] = tempi


def partition (array, p, r):
    # string = f'p:{p} r:{r} {array} '
    x = array[r - 1] 
    i = p - 1 
    for j in range(p, r - 1):
        if (array[j] <= x):
            i = i + 1
            exchange(array, i, j) 
    exchange(array, i + 1, r - 1)
    # string += f'--> ${array}' ; print(string)
    return i + 1 


def quicksort(array, p, r):
    
    if (p < r):
        q = partition(array, p, r) 
        quicksort(array, p, q - 1)
        quicksort(array, q + 1, r)


# example_array = [2, 8, 7, 1, 3, 5, 6, 4] 

# print(example_array)
# quicksort(example_array, 0, len(example_array)) 
# print(example_array)

random.seed() 
hold_numbers = []

for i in range(1000000):
    hold_numbers.append(random.randint(0, 100000000))

def quicksort_wrapper () :
    quicksort(hold_numbers, 0, len(hold_numbers))
 

elapsed_time = timeit.timeit(quicksort_wrapper, number=10)

print(elapsed_time)
