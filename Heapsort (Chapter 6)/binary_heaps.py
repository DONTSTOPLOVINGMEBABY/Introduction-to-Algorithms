'''
An array A[1 : n] that represents a heap is an object with an attribute A.heap-size, 
which represents how many elements in the heap are stored with an array A. That is, 
although A[1:N] may contain numbers, only the elements in A[1:A.heap-size], where 0 ≤
A.heap-size ≤ n, are valid elements of the heap. If A.heap-size = 0, then the heap is empty. The 
root of the tree is A[1], and given the index i of a node, there is a way to compute the indices of its parent,
left-child, and right-child with one-line procedures. 

'''

class HeapObject : 
    def __init__(self, data=[]):
        self.heap = data
        self.heap_size = len(data) - 1

    def push_to_heap(self, item):
        self.heap.append(item)
        self.heap_size += 1 
    
    def parent(self, i):
        return i // 2
    
    def left(self, i):
        return 2 * i 
    
    def right(self, i):
        return (2 * i) + 1 
    
    def exchange(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp


array = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
heap = HeapObject()
for i in array:
    heap.push_to_heap(i)

print(heap.heap[heap.parent(5)])