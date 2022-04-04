from typing import Optional, List
import unittest

class Node:
    '''
    Represents Data Node
    '''

    def __init__(self, key: int, val: str, front: Optional["Node"] = None, back: Optional["Node"] = None):

        self.key: int = key
        self.val: str = val
        self.front: Optional["Node"] = front
        self.back: Optional["Node"] = back

    def __repr__(self):

        return str(self.__dict__)

class TestNode(unittest.TestCase):
    '''
    Test Data Node Operations
    '''

    def testSingleNode(self):

        node1 = Node(1, "Test")
        self.assertEqual(node1.front, None, "Node Test | Front must be None for single Node")
        self.assertEqual(node1.back, None, "Node Test | Back must be None for single Node")

    def testNodeLinking(self):

        node1 = Node(1, "Test")
        node2 = Node(2, "Test2", front = node1)
        node1.back = node2
        self.assertEqual(node1.back, node2, "Node Test | Back must be assigned")
        self.assertEqual(node2.front, node1, "Node Test | Front must be assigned")


class LRUCache:

    '''
    LRU Cache Implementation
    '''

    def __init__(self, capacity: int = 5):

        self.capacity: int = capacity
        self.currentCapacity: int = 0
        self.head: Optional["Node"] = None
        self.tail: Optional["Node"] = None
        self.data: dict[int, "Node"] = dict()

    def __repr__(self):

        result = "\n"
        result += "Capacity : {}\n".format(self.capacity)
        result += "Current Capacity : {}\n".format(self.currentCapacity)
        result += "Head : {}\n".format(self.head.key if self.head else None)
        result += "Tail : {}\n".format(self.tail.key if self.tail else None)
        entries: List[str] = []
        for key, node in self.data.items():
            entries.append(("{} -> {}".format(key, node.val)))
        result += "Data : {}\n".format(" | ".join(entries))
        return result

    def _getCurrentCapacity(self) -> int:
        
        return self.currentCapacity

    def _isFull(self) -> bool:

        if (self.capacity == self.currentCapacity):
            return True
        else:
            return False

    def _evictLast(self) -> None:

        if (self.tail):
            lastNode = self.tail
            self.tail = lastNode.front # Reassign tail of LRUCache
            del self.data[lastNode.key] # delete last node
            self.currentCapacity -= 1 # Reduce capacity by 1

    def _moveUp(self, node: "Node") -> None:

        # if node is the head, do nothing
        if (self.head == node):
            return

        # if node is the first element, assign node to head
        if (self.head == None and self.tail == None):
            self.head = node
            self.tail = node
            return

        # Update tail if node is last
        if (self.tail == node):
            self.tail = node.front

        # get reference to head, node.front and node.back
        currentHead = self.head
        nodeFront = node.front
        nodeBack = node.back
        
        # Move node up as head
        self.head = node
        node.back = currentHead
        node.front = None
        currentHead.front = node

        # Reassign node position's front and back
        if nodeFront:
            nodeFront.back = nodeBack
        if nodeBack:
            nodeBack.front = nodeFront



    def get(self, key: int) -> Optional[str]:

        if (key in self.data):
        # if key found, move up the node, return the node
            node = self.data[key]
            self._moveUp(node)
            return node.val
        else:
        # if key not found, return None
            return None

    def put(self, key: int, val: str) -> "LRUCache":
        
        if (key in self.data):
        # if key found, update the node, move up the node
            node = self.data[key]
            node.val = val
            self._moveUp(node)
        else:
        # if new key, create new Node, move up the node
            if (self._isFull()):
                self._evictLast()
            newNode = Node(key, val)
            self._moveUp(newNode)
            self.data[key] = newNode
            self.currentCapacity += 1

        return self

class TestLRUCache(unittest.TestCase):

    '''
    Test LRU Cache Operations
    '''

    def testCapacity(self):

        cache = LRUCache(3)
        cache.put(1,"a").put(1,"b")
        self.assertEqual(cache._getCurrentCapacity(), 1, "#1 Test Capacity")
        cache.put(2,"c")
        self.assertEqual(cache._getCurrentCapacity(), 2, "#2 Test Capacity")
        cache.put(3,"c").put(4,"c")
        self.assertEqual(cache._getCurrentCapacity(), 3, "#3 Capacity must remain at the set limit")


    def testLRUCachePut(self):

        cache = LRUCache(3)
        cache.put(1,"a").put(2,"b").put(3,"c")
        self.assertEqual(cache.head.val, "c", "#1 Head updated")
        self.assertEqual(cache.tail.val, "a", "#1 Tail remains unchanged")
        self.assertEqual(cache.currentCapacity, 3, "#1 Capacity must update")
        self.assertEqual(cache.get(1), "a", "# Put persists data")
        self.assertEqual(cache.currentCapacity, 3, "#1 Capacity must update")
        cache.put(4,"z")
        self.assertEqual(cache.get(2), None, "# Tail eviction")
        
    def testLRUCacheGet(self):
        cache = LRUCache(capacity = 3)
        cache.put(1,"a").put(2,"b")
        self.assertEqual(cache.get(1), "a", "Key lookup match")
        self.assertEqual(cache.get(2), "b", "Key lookup match")
        self.assertEqual(cache.get(3), None, "Key lookup not found")
        cache.put(1,"z")
        self.assertEqual(cache.get(1), "z", "Key lookup match")

    def testLRUEviction(self):
        cache = LRUCache(capacity = 2)
        cache.put(1,"a").put(2,"b").put(3,"c")
        self.assertEqual(cache.head.val, "c", "Head should be 3")
        self.assertEqual(cache.tail.val, "b", "Head should be 2")

if __name__ == "__main__":
    unittest.main()