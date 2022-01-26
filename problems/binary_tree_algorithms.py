
## https://www.youtube.com/watch?v=fAAZixBzIAI


class Node:
    
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.__dict__)
    
class Tree:
    
    def __init__(self, root = None):
        self.root = root
        
    def isEmpty(self):
        if (self.root == None):
            return True
        else:
            return False
        
    def dfsWithStackIteration(self):
        
        if (self.isEmpty()):
            return
        
        stack = Stack()
        stack.push(self.root)
        
        ll = LinkedList()
        
        while (not stack.isEmpty()):
            node = stack.pop().data
            if node.right:
                stack.push(node.right)
            if node.left:
                stack.push(node.left)
            ll.append(node.data)

        ll.inspect()
        
    def dfsRec(self):
        result = self._dfsWithRecursion(self.root)
        result.inspect()
        
        
    def _dfsWithRecursion(self, node:Node = None, ll:LinkedList = LinkedList()):
        
        if (node == None):
            return
        else:
            self._dfsWithRecursion(node.left, ll)
            self._dfsWithRecursion(node.right, ll)
            ll.append(node.data)
            
        return ll
    
    def _bfs(self, q:Queue = Queue(), ll:LinkedList = LinkedList()):
        
        while (not q.isEmpty()):
            node = q.deQ()
            ll.append(node.data)
            if (node.left):
                q.enQ(node.left)
            if (node.right):
                q.enQ(node.right)
        
        return ll
    
    def bfsIter(self):
        
        if (self.isEmpty()):
            return None
        else:
            q = Queue()
            q.enQ(self.root)
            return self._bfs(q)
        
    def _dfsExists(self, key, node):
        
        if (node == None):
            return False
        else:
            if (node.data == key):
                return True
            else:
                return self._dfsExists(key, node.left) or self._dfsExists(key, node.right)
            
    def dfsExists(self, key):
        
        return self._dfsExists(key, self.root)
    
    def _bfsExists(self, key, q:Queue):
        
        if (q.isEmpty()):
            return False
        else:
            node = q.deQ()
            if (node.data == key):
                return True
            else:
                if (node.left):
                    q.enQ(node.left)
                if (node.right):
                    q.enQ(node.right)
                return self._bfsExists(key, q)
                
    def bfsExists(self, key):
        q = Queue()
        if (self.isEmpty()):
            return False
        else:
            q.enQ(self.root)
            return self._bfsExists(key, q)
        
        
        
    def _dfsGetSumIter(self, node:Node = None):
        if (node == None):
            return 0
        else:
            return node.data + self._dfsGetSumIter(node.left) + self._dfsGetSumIter(node.right)
        
    def dfsGetSumIter(self):
        return self._dfsGetSumIter(self.root)
    
    
    def dfsGetSumRec(self):
        
        s = 0
        
        if (self.isEmpty()):
            return s
        
        stack = Stack()
        stack.push(self.root)
        
        while (not stack.isEmpty()):
            node = stack.pop().data
            s += node.data
            if (node.left):
                stack.push(node.left)
            if (node.right):
                stack.push(node.right)
        
        return s
    
    def bfsGetSumRec(self):
        
        s = 0 
        
        if (self.isEmpty()):
            return s
        
        q = Queue()
        q.enQ(self.root)
        
        while (not q.isEmpty()):
            
            node = q.deQ()
            print(node.data)
            
            s += node.data
            if (node.left):
                q.enQ(node.left)
            if (node.right):
                q.enQ(node.right)
                
        return s
    
    
    def _dfsFindMinRec(self, node):
        
        if (node == None):
            return float('inf')
        else:
            return min(node.data, self._dfsFindMinRec(node.left), self._dfsFindMinRec(node.right))
        
    def dfsFindMinRec(self):
        
        if (self.isEmpty()):
            return None
        else:
            return self._dfsFindMinRec(self.root)
        
        
    def bfsFindMinIter(self):
        
        if (self.isEmpty()):
            return None
        
        m = float('inf')
        
        q = Queue()
        
        q.enQ(self.root)
        
        while (not q.isEmpty()):
            node = q.deQ()
            m = min(m,node.data)
            if (node.left):
                q.enQ(node.left)
            if (node.right):
                q.enQ(node.right)
                
        return m
        
    def dfsFindMinIter(self):
        
        if (self.isEmpty()):
            return None
        
        m = float('inf')
        
        stack = Stack()
        
        stack.push(self.root)
        
        while (not stack.isEmpty()):
            node = stack.pop().data
            
            m = min(m, node.data)
            
            if (node.left):
                stack.push(node.left)
                
            if (node.right):
                stack.push(node.right)
                
        return m
    
    
    def _dfsCollectParentsIter(self, node, d = dict(), c = []):
        
        if (node == None):
            return
        
        if (node.left == None and node.right == None):
            c.append(node)
            
        if (node.left):
            d[node.left] = node
            self._dfsCollectParentsIter(node.left, d, c)
        
        if (node.right):
            d[node.right] = node
            self._dfsCollectParentsIter(node.right, d, c)
            
        return d,c
    
    def dfsCollectParentsIter(self):
        
        d = dict()
        c = []
        if (self.isEmpty()):
            return d,c
        else:
            return self._dfsCollectParentsIter(self.root, d)
        
        
    def findPath(self, childNode, parents: dict):
        
        node = childNode
        path = []
        
        while (node):
            path.append(node.data)
            node = parents.get(node, None)
            
        return path
    
    
    def _recSum(self, node, path = [], paths = []):
        
        if (node):
            # print(node, path, paths)
            path.append(node)
            if (node.left):
                self._recSum(node.left, path.copy(), paths)
            if (node.right):
                self._recSum(node.right, path.copy(), paths)
            if (node.left == None and node.right == None):
                paths.append(path)
        else:
            return
            
    def recSum(self):
        paths = []
        if (not self.isEmpty()):
            self._recSum(self.root, [], paths)
        return paths
    
    def _recSum1(self, node, prevSum=0):
        
        if (node):
            newSum = prevSum + node.data
            if (node.left == None and node.right == None):
                return prevSum + node.data
            leftSum = self._recSum1(node.left, newSum)
            rightSum = self._recSum1(node.right, newSum)
            return max(leftSum, rightSum)
        else:
            return 0
            
        
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# tree = Tree(a)

# res = tree.bfsIter()
# res.inspect()

# print(tree.dfsExists("g"))
# print(tree.bfsExists("g"))


# tree.dfsWithStackIteration()

# tree.dfsRec()


# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(2)
# f = Node(1)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# tree = Tree(a)

# print(tree.dfsGetSumIter())
# print(tree.dfsGetSumRec())
# print(tree.bfsGetSumRec())

# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(2)
# f = Node(10)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# tree = Tree(a)

# print(tree.dfsFindMinRec())
# print(tree.dfsFindMinIter())
# print(tree.bfsFindMinIter())


a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(21)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

tree = Tree(a)

# m = float('-inf')
# for path in tree.recSum():
#     m1 = 0
#     for node in path:
#         m1 += node.data
#     m = max(m, m1)
# print(m)

print(tree._recSum1(tree.root))

# p,c = tree.dfsCollectParentsIter()
# print(p[b])
# print(c)

# mr = 0
# for child in c:
#     mr = max(mr, sum(tree.findPath(child,p)))
    
# print(mr)



