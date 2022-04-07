from typing import Optional
import unittest
import inspect
import collections

class TreeNode(object):

    def __init__(self, val: int, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):

        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):

        left = None if not self.left else self.left.val
        right = None if not self.right else self.right.val

        res = """Value : {} | Left Value : {} | Right Value : {}""".format(self.val, left, right)

        return res

class TestTreeNode(unittest.TestCase):

    def testNodeFormation(self):

        print("*** Executing Test Case {} ***".format(inspect.currentframe().f_code.co_name))

        n1 = TreeNode(1)
        n2 = TreeNode(2, left = n1)
        n3 = TreeNode(3)
        n2.right = n3

        self.assertEqual(n2.left, n1, "testNodeFormation | Left Assignment")
        self.assertEqual(n2.right, n3, "testNodeFormation | Right Assignment")
        self.assertEqual(n1.left, None, "testNodeFormation | None Assignment")
        self.assertEqual(str(n2), "Value : 2 | Left Value : 1 | Right Value : 3", "testNodeFormation | Stringify")


class Codec:

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        q = collections.deque()
        res = []

        q.append(root)

        while q:
            thisNode = q.popleft()
            if (thisNode):
                res.append(str(thisNode.val))
                q.append(thisNode.left)
                q.append(thisNode.right)
            else:
                res.append("x")

        return "|".join(res)

        

    def deserialize(self, data: str) -> "TreeNode":
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        nodes = data.split("|")
        rootVal = nodes.pop(0)
        rootNode = TreeNode(rootVal)
        q = collections.deque()
        q.append(rootNode)

        while q and nodes:

            node = q.popleft()
            if (nodes):
                leftVal = nodes.pop(0)
                if (leftVal != "x"):
                    newNode = TreeNode(leftVal)
                    node.left = newNode
                    q.append(newNode)
            if (nodes):
                rightVal = nodes.pop(0)
                if (rightVal != 'x'):
                    newNode = TreeNode(rightVal)
                    node.right = newNode
                    q.append(newNode)

        return rootNode

class TestCodec(unittest.TestCase):

    def setUp(self):
        self.codec = Codec()

    def testSerialize(self):

        print("*** Executing Test Case {} ***".format(inspect.currentframe().f_code.co_name))

        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n6 = TreeNode(6)
        n1.left = n2
        n1.right = n6
        n2.left = n3

        self.assertEqual(self.codec.serialize(n1), "1|2|6|3|x|x|x|x|x", "testSerialize | 1|2|6|3|x|x|x|x|x")

    def testDeserialize(self):

        input = "1|2|6|3|x|x|x|x|x"
        expected = ['1','2','6','3']
        node = self.codec.deserialize(input)

        q = collections.deque()
        res = []
        q.append(node)
        while q:
            thisNode = q.popleft()
            res.append(thisNode.val)
            if (thisNode.left):
                q.append(thisNode.left)
            if (thisNode.right):
                q.append(thisNode.right)

        self.assertEqual(res, expected, "Test Code Deserialize")


if (__name__ == "__main__"):
    unittest.main()