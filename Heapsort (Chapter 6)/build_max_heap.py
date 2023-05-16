from max_heapify import Max_Heapify
from binary_heaps import HeapObject

def Build_Max_Heap (A, n) :
    
    i = n // 2
    while i > 0 :
        Max_Heapify(A, i) 
        i -= 1 

array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heap = HeapObject(array)
print(heap.heap)
Build_Max_Heap(heap, len(heap.heap))
print(heap.heap)




#  Output array should be : 
#  [ 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 ]