
def sum(l,acc=0):
    """
    Returns the sum of integers
    
    Parameters:
        l(list) : List of integers
    Returns:
        (integer) : the sum of list of integers
    """

    l = list(l)
    if(l):
        val = l.pop()
        acc += val
        return sum(l,acc)
    else:
        return acc

def mul(l,acc=1):
    """
    Returns the product of integers
    
    Parameters:
        l(list) : List of integers
    Returns:
        (integer) : the product of list of integers
    """

    l = list(l)
    if(l):
        item = l.pop()
        acc*=item
        return (mul(l,acc))
    else:
        return acc

#print(sum([1,2,3,4]))
#10
#print(mul([1,2,3,4]))
#24



def reverseString(s):
    
    print(s)
    if (not s):
        return ""
    
    if (len(s) == 1):
        return s[0]
    else:
        return reverseString(s[1:]) + s[0] 
    
# print(reverseString("recursion"))


def isPalindrome(s, start = None, end = None):
    
    
    start = 0 if not start else start
    end = len(s) - 1 if not end else end
    print(s[start:end+1])
    
    if (start >= end): 
        return True
    
    if (s[start] == s[end]):
        return isPalindrome(s, start+1, end-1)
    else:
        return False
    
# print(isPalindrome("1kayyak1"))
# print(isPalindrome("1kayak1"))

def isPalindrome(s):
    
    print(s)
    if (len(s) <= 1): 
        return True
    
    if (s[0] == s[len(s)-1]):
        return isPalindrome(s[1:len(s)-1])
    else:
        return False


# print(isPalindrome("1kayyak1"))
# print(isPalindrome("1kayak1"))


def binaryOf(num):
    
    
    q = num // 2
    r = num % 2
    print(num, q, r)
    if q == 0:
        return str(r)
    else: 
        return binaryOf(q) + str(r)

# print(binaryOf(3))


def sumNatural(num):
    
    if num == 1:
        return 1
    else:
        return num + sumNatural(num-1)
    
# print(sumNatural(10))


# import time


def binarySearch(arr, num, s = None, e = None):
    
    # time.sleep(0.1)
    
    s = 0 if not s else s
    e = len(arr) - 1 if not e else e
    middle = (s+e) // 2
    print(arr[s:e], s, e, middle)
    
    if (s > e):
        return -1
    
    if (arr[middle] == num):
        return middle
    
    if (num < arr[middle]):
        return binarySearch(arr, num, s, middle-1)
    else:
        return binarySearch(arr, num, middle+1, e)
    
    
    
# print(binarySearch([-1, 10, 20, 33, 41,43], 20))


def fib(n, d = dict()):
    
    if n in d:
        return d[n]
    
    if n <=1:
        return n
    
    d[n]=  fib(n-2) + fib(n-1)
    return d[n]

# print(fib(50))

def merge(a, b):
    
    e1 = len(a)-1
    e2 = len(b)-1
    s1 = 0
    s2 = 0
    
    result = []
    
    while (s1 <= e1 and s2 <= e2):
        if a[s1] <= b[s2]:
            result.append(a[s1])
            s1+=1
        else:
            result.append(b[s2])
            s2+=1
    
        
    while s1 <= e1:
        result.append(a[s1])
        s1+=1
        
    while s2 <= e2:
        result.append(b[s2])
        s2+=1
    
    return result

# print(merge([30], [20]))
        

def mergeSort(nums):
    
    if (len(nums) <= 1):
        return nums
    
    middle = len(nums) // 2
    left = nums[0:middle]
    right = nums[middle:]
    
    return merge(mergeSort(left), mergeSort(right))

import random
num2 = list(range(1,30,3))
random.shuffle(num2)
print(num2)
print(mergeSort(num2))

def mergeSort(nums, s = None, e = None):
    
    if (len(nums) <= 1):
        return nums
    
    s = 0 if not s else s
    e = len(nums) - 1 if not e else e
    m = (s+e)//2
    
    return merge(mergeSort(nums,s,m), mergeSort(nums,m+1,e))

#import random
#num2 = list(range(1,30,3))
#random.shuffle(num2)
#print(num2)
#print(mergeSort(num2))

class ListNode:
    
    def __init__(self, data, back = None):
        self.data = data
        self.next = back
        
    def __repr__(self):
        return str(self.__dict__)
    
    
a = ListNode("a")
b = ListNode("b", a)
c = ListNode("c", b)
d = ListNode("d", c)

# print(d)

def reverseList(node):
    
    currNode = node
    prevNode = None
    
    while currNode:
        tmp = currNode.next
        # print(prevNode, currNode, tmp)
        currNode.next = prevNode
        prevNode = currNode
        currNode = tmp
        
    return prevNode

# print(reverseList(d))
    
def reverseListRec(currNode, prevNode = None):
    
    if (currNode == None):
        return prevNode
    
    tmp = currNode.next
    currNode.next = prevNode
    prevNode = currNode

    return reverseListRec(tmp, prevNode)

# print(reverseListRec(d))
    
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n3
n3.next = n5
n2.next = n4

# print(n1)
# print(n2)
        
def mergeSortedLinkedList(a, b):
    
    if (a == None):
        return b
    if (b == None):
        return a
    
    if (a.data <= b.data):
        a.next = mergeSortedLinkedList(a.next, b)
        return a
    else:
        b.next = mergeSortedLinkedList(b.next, a)
        return b
    
# print(mergeSortedLinkedList(n1, n2))


class TreeNode:
    
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
    def __repr__(self):
        return str(self.__dict__)

    
def insertIntoBSTreeRec1(node, data):
    
    if node == None:
        return
    
    if node.data == data:
        return
    
    if (data <= node.data):
        if (node.left):
            insertIntoBSTreeRec1(node.left, data)
        else:
            node.left = TreeNode(data)
    else:
        if (node.right):
            insertIntoBSTreeRec1(node.right, data)
        else:
            node.right = TreeNode(data)
            

n10 = TreeNode(10)
n8 = TreeNode(8)
n4 = TreeNode(4)
n9 = TreeNode(9)
n12 = TreeNode(12)
n8.left = n4
n8.right = n9
n10.left = n8
n10.right = n12

# print(n10)
# insertIntoBSTreeRec1(n10, 5)
# print(n10)

def insertIntoBSTreeRec(data, node = None):
    
    if node == None:
        return TreeNode(data)
    
    if node.data == data:
        return node
    
    if (data <= node.data):
        node.left = insertIntoBSTreeRec(data, node.left)
    else:
        node.right = insertIntoBSTreeRec(data, node.right)

    return node

n1 = None
for num in [20,5,4,6,3,7,9,40]:
    n1 = insertIntoBSTreeRec(num, n1)
# print(n1)
        
def printAllLeaves(treeNode):
    
    if (treeNode == None):
        return
    
    if (not treeNode.left and not treeNode.right):
        print(treeNode.data)
        
    printAllLeaves(treeNode.left)
    printAllLeaves(treeNode.right)

# printAllLeaves(n1)

#          20
#        5    40
#      4   6
#    3       7
#              9
    
    
graph = {
    "a" : ["b"],
    "b" : ["c"],
    "c" : ["d"],
    "d" : ["e", "g"],
    "g" : ["h"],
    "h" : [],
    "e" : ["f"],
    "f" : ["i", "j", "k"],
    "i" : [],
    "j" : [],
    "k" : ["a"]
}

# print(graph)

def bfsGraph(graph, node, visited = set()):
    
    q = [node]
    path = []
    
    while q:
        currNode = q.pop(0)
        if currNode not in visited:
            visited.add(currNode)
            path.append(currNode)
            adjacentNodes = graph.get(currNode, [])
            for node in adjacentNodes:
                q.append(node)
            
    print(path)
    
def dfsGraphIter(graph, node, visited = set()):
    
    s = [node]
    path = []
    
    while s:
        currNode = s.pop()
        if currNode not in visited:
            visited.add(currNode)
            path.append(currNode)
            adjNodes = graph.get(currNode, [])
            for node in adjNodes:
                s.append(node)
            
    print(path)
    
def dfsGraphRec(graph, node, path, visited = set()):
    
    if (len(path) == 0):
        path = [node]
        visited.add(node)

    for adjNode in graph[node]:
        if adjNode not in visited:
            path.append(adjNode)
            visited.add(adjNode)
            dfsGraphRec(graph, adjNode, path)
    
    return path

    
# bfsGraph(graph, "a")
# dfsGraphIter(graph, "a")
# print(dfsGraphRec(graph, "a", []))


    
    
    



