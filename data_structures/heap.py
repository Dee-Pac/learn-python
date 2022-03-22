class MinHeap:

    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def push(self, element):
        self.heap.append(element)
        self._percolateUp(len(self.heap)-1)
        return self

    def _parent(self, index):
        parent = (index-1)//2
        if (parent < 0):
            return None
        else:
            return parent

    def _children(self, index):
        offset = index * 2 
        return offset + 1, offset + 2

    def _percolateUp(self, index):
        
        parentIndex = self._parent(index)
        if (parentIndex == None):
            return
        if (self.heap[index] < self.heap[parentIndex]):
            tmp = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = tmp
            self._percolateUp(parentIndex)

    def pop(self):
        res = None
        if (self.heap):
            res = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self._remax(0)
        return res

    def _remax(self, index):

        left, right = self._children(index)
        minIndex = None

        if (left < len(self.heap) and self.heap[left] < self.heap[index]):
            minIndex = left
        elif (right < len(self.heap) and self.heap[right] < self.heap[index]):
            minIndex = right
        else:
            pass

        if minIndex:
            tmp = self.heap[index]
            self.heap[index] = self.heap[minIndex]
            self.heap[minIndex] = tmp
            print(self.heap)
            self._remax(minIndex)

    def heapify(self, l):

        for i in range(len(l)):
            self.heap.append(l[i])
            self._percolateUp(i)


heap = MinHeap()
heap.push(1).push(2).push(3).push(4).push(5)

# Test Children of Node
assert(heap._children(0) == (1,2))
assert(heap._children(1) == (3,4))
assert(heap._children(2) == (5,6))
assert(heap._children(3) == (7,8))

# Test Parent of Node
assert(heap._parent(0) == None)
assert(heap._parent(1) == 0)
assert(heap._parent(2) == 0)
assert(heap._parent(5) == 2)
assert(heap._parent(8) == 3)

# Test Push
heap = MinHeap()
heap.push(10)
assert(heap.heap[0] == 10)
heap.push(1)
assert(heap.heap[0] == 1)
heap.push(20)
assert(heap.heap[0] == 1)
heap.push(-1)
assert(heap.heap[0] == -1)
# print(heap)


# Test Pop
heap = MinHeap()
heap.push(1).push(2)
assert(heap.pop() == 1)
assert(heap.pop() == 2)
assert(heap.pop() == None)

heap.push(1).push(2).push(-1).push(-2)

assert(heap.pop() == -2)
assert(heap.pop() == -1)
assert(heap.pop() == 1)
assert(heap.pop() == 2)
assert(heap.pop() == None)

# Test Heapify
heap = MinHeap()
heap.heapify([10,20,-1,2])
print(heap)



