'''
Max-Heapify maintains the max-heap property. Its inputs are an array A with the heap-size attribute and an index i. 
When it's called, Max-Heap asumes that the binary trees rooted at Left(i) and Right(i) are max-heaps but that
A[i] might be smaller than its children, thus violating the max-heap property. 
'''

'''
Max-Heapify in Plain English 

i <-- current node 
array <-- the heap itself 
left <-- gets the left child of i 
right <-- gets the right child of i  

Max-Heapify(Array, i)

    l = left(i)                                 # l represents the index of the left element in the array 
    r = right(i)                                # r represents the index of the right element in the array 
    if (l <= Array.heap-size and A[l] > A[i]):  # If l index is within the list (smaller than Array.heap-size) and the left 
        largest = l                             # node is bigger than the current, then set largest to l 
    else : largest = i                          # if the current node is bigger than l, than largest = l 
    if (r <= Array.heap-size and A[r] > A[largest]): # Same as above but with right node. If right is bigger, 
        largest = r                             # largest becomes right node
    if largest != i :                           # if the largest node out of the three was the original, don't continue 
        exchange A[i] with A[largest]           # if the largest node out of the three was left or right, swap the largest 
        Max-Heapify( A, largest )               # with the current root and call Max-Heapify again with array and largest as the new root index
                                                # because we just switched our intial root (4) into the largest position 
''' 


from binary_heaps import HeapObject

def Max_Heapify(HeapObject, i):
    left = HeapObject.left(i) - 1 
    right = HeapObject.right(i) - 1 
    i -= 1 
    if left <= HeapObject.heap_size and HeapObject.heap[left] > HeapObject.heap[i] :
        largest = left 
    else : largest = i
    if right <= HeapObject.heap_size and HeapObject.heap[right] > HeapObject.heap[largest] : 
        largest = right
    if largest != i :
        HeapObject.exchange(i, largest)
        Max_Heapify(HeapObject, largest + 1)  # Account for -1 above

heap_array = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
heap = HeapObject(heap_array)
Max_Heapify(heap, 2)
# print(heap.heap)