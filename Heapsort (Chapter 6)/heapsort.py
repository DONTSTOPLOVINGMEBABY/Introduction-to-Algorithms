'''
Psuedo-Code 

HEAPSORT(A, n)
    BUILD-MAX-HEAP(A, N)
    for i = n downto 2 
        exchange A[i] with A[i]
        A.heap-size = A.heap-size - 1 
        MAX-HEAPIFY(A, 1)
'''

from binary_heaps import HeapObject
from build_max_heap import Build_Max_Heap
from max_heapify import Max_Heapify

def Heapsort(A, n):
    Build_Max_Heap(A, n)
    i = n 
    while i > 1 : 
        A.exchange(0, i - 1)
        A.heap_size -= 1 
        Max_Heapify(A, 1)
        i -= 1 










array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heap = HeapObject(array)
Heapsort(heap, len(heap.heap))
print(heap.heap)