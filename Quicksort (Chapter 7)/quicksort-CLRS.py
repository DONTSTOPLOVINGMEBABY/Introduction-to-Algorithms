def partition (array, p, r):
    string = f'p:{p} r:{r} {array} '
    x = array[r - 1] 
    i = p - 1 
    for j in range(p, r - 1):
        if (array[j] <= x):
            i = i + 1
            tempi = array[i]
            tempj = array[j] 
            array[i] = tempj
            array[j] = tempi 
    temp_i_plus_1 = array[i + 1] 
    array[i + 1] = x 
    array[r - 1] = temp_i_plus_1
    string += f'--> ${array}' ; print(string)
    return i + 1 


def quicksort(array, p, r):
    
    if (p < r):
        q = partition(array, p, r) 
        quicksort(array, p, q - 1)
        quicksort(array, q + 1, r)


example_array = [2, 8, 7, 1, 3, 5, 6, 4] 

print(example_array)
quicksort(example_array, 0, len(example_array)) 
print(example_array)

