def InsertionSort (array, n):
    
    for i in range(1, n):
        key = array[i]
        j = i - 1 
        while j > -1 and array[j] > key : 
            array[j + 1] = array[j]
            j = j - 1 
        array[j + 1] = key

unsorted_arr = [5, 2, 4, 6, 1, 3]
InsertionSort(unsorted_arr, len(unsorted_arr))
print(unsorted_arr)


'''
Run time (best case) = O(n) if all elements are sorted (loop through all elements but no swapping is required)

Run time (worst case) = O(n^2) if elements are hardly sorted (lots of swaps have to be done)

Space-Complexity = Constant given that the array is sorted in place and the same amount of space is used to 
store the key regardless of the input size of the initial array. 

'''