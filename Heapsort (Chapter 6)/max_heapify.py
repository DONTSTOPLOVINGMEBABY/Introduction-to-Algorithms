'''
Max-Heapify maintains the max-heap property. Its inputs are an array A with the heap-size attribute and an index i. 
When it's called, Max-Heap asumes that the binary trees rooted at Left(i) and Right(i) are max-heaps but that
A[i] might be smaller than its children, thus violating the max-heap property. 
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
print(heap.heap)
