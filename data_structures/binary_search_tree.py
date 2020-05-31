# Required for Level Order traversal 
 
class QNode:
    def __init__(self,data,nxt= None):
        self.data = data
        self.nxt = nxt

    def __repr__(self):
        return str(self.data)

# Required for Level Order traversal 

class Q:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return (self.head == None)

    def enq(self,data):
        new_node = QNode(data)
        if (not self.is_empty()):
            self.tail.nxt = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        return self

    def dq(self):
        if (not self.is_empty()):
            k = self.head
            self.head = self.head.nxt
            return k
        else:
            return None

    def __repr__(self):
        s = ""
        node = self.head
        while (node):
            s+= str(node.data) + "<-"
            node = node.nxt
        return s
            

q = Q()
q.enq(1).enq(2).enq(3).enq(4)
print(q)
# 1<-2<-3<-4<-
q.dq()
print(q)
# 2<-3<-4<-
q.dq()
k = q.dq()
print(k,q)
# (3, 4<-)


class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        self.children_counter = 0

    def __repr__(self):
        left_data = self.left.data if self.left else ""
        right_data = self.right.data if self.right else ""
        s = "left [{}] | data [{}] right | [{}] total children | [{}]".format(left_data,self.data,right_data,self.children_counter)
        return s

    def pre_order(self):
        print(self)
        if (self.left): self.left.pre_order()
        if (self.right): self.right.pre_order()
    
    def in_order(self):
        if (self.left): self.left.in_order()
        print(self)
        if (self.right): self.right.in_order()
    
    def post_order(self):
        if (self.left): self.left.in_order()
        if (self.right): self.right.in_order()
        print(self)  

    def append(self,data):
        print("traversing [{}] ".format(self.data))
        if (data <= self.data):
            if (self.left):
                self.left.append(data)
            else:
                new_node = Node(data)
                self.left = new_node
                print("added [{}] at left of [{}]".format(data,self.data))
        else:
            if (self.right):
                self.right.append(data)
            else:
                new_node = Node(data)
                self.right = new_node
                print("added [{}] at right of [{}]".format(data,self.data))
        self.children_counter +=1
        return self
    
    def find(self,data,parent=None,get_parent=False):
        print("traversing [{}] ".format(self.data))
        if (self.data == data):
            print("found [{}]".format(self))
            if (get_parent):
                return self,parent
            else: 
                return self
        elif (data < self.data and self.left):
            self.left.find(data)
        elif (data > self.data and self.right):
            self.right.find(data)
        else:
            print("NOT found [{}]".format(data))
            return None

class BST:
    def __init__(self):
        self.root = None

    # Youtube reference https://www.youtube.com/watch?v=86g8jAQug04
    def print_pre_order(self):
        print("---- pre order ----")
        if (self.root):
            self.root.pre_order()
        else:
            print("---- EMPTY ----")
    
    def print_in_order(self):
        print("---- in order ----")
        if (self.root):
            self.root.in_order()
        else:
            print("---- EMPTY ----")
    
    def print_post_order(self):
        print("---- post order ----")
        if (self.root):
            self.root.post_order()
        else:
            print("---- EMPTY ----")

    # Youtube reference https://www.youtube.com/watch?v=86g8jAQug04
    def print_level_order(self,q=None):
        if (self.root == None):
            print("---- EMPTY ----")
            return
        if (q==None):
            print("---- level order ----")
            q = Q()
            q.enq(self.root)
        if (not q.is_empty()):
            node = q.dq().data
            print(node)
            if (node.left): 
                q.enq(node.left)
            if (node.right): 
                q.enq(node.right)
            self.print_level_order(q)
        else:
            print("--- END Level Order ----")

    def find(self,data):
        print("---- Looking for [{}] ----".format(data))
        if (self.root == None):
            return None
        else:
            return self.root.find(data)

    def append(self,*data):
        if (self.root == None):
            first = data[0]
            rest = data[1::]
            self.root = Node(first)
            for element in rest:
                self.root.append(element)
        else:
            for element in data:
                self.root.append(element)
        return self
        

t = BST()
t.append(15).append(10).append(20)
t.append(8,6,12,17,25,16,27)
t.find(12)
# ---- Looking for [12] ----
# traversing [15] 
# traversing [10] 
# traversing [12] 
# found [left [] | data [12] right | [] total children | [0]]
t.find(27)
# ---- Looking for [27] ----
# traversing [15] 
# traversing [20] 
# traversing [25] 
# traversing [27] 
# found [left [] | data [27] right | [] total children | [0]]
t.find(9)
# ---- Looking for [9] ----
# traversing [15] 
# traversing [10] 
# traversing [8] 
# NOT found [9]

t.print_pre_order()
# ---- pre order ----
# left [10] | data [15] right | [20] total children | [10]
# left [8] | data [10] right | [12] total children | [3]
# left [6] | data [8] right | [] total children | [1]
# left [] | data [6] right | [] total children | [0]
# left [] | data [12] right | [] total children | [0]
# left [20] | data [20] right | [25] total children | [5]
# left [17] | data [20] right | [] total children | [2]
# left [16] | data [17] right | [] total children | [1]
# left [] | data [16] right | [] total children | [0]
# left [] | data [25] right | [27] total children | [1]
# left [] | data [27] right | [] total children | [0]
t.print_in_order()
# ---- in order ----
# left [] | data [6] right | [] total children | [0]
# left [6] | data [8] right | [] total children | [1]
# left [8] | data [10] right | [12] total children | [3]
# left [] | data [12] right | [] total children | [0]
# left [10] | data [15] right | [20] total children | [10]
# left [] | data [16] right | [] total children | [0]
# left [16] | data [17] right | [] total children | [1]
# left [17] | data [20] right | [] total children | [2]
# left [20] | data [20] right | [25] total children | [5]
# left [] | data [25] right | [27] total children | [1]
# left [] | data [27] right | [] total children | [0]
t.print_post_order()
# ---- post order ----
# left [] | data [6] right | [] total children | [0]
# left [6] | data [8] right | [] total children | [1]
# left [8] | data [10] right | [12] total children | [3]
# left [] | data [12] right | [] total children | [0]
# left [] | data [16] right | [] total children | [0]
# left [16] | data [17] right | [] total children | [1]
# left [17] | data [20] right | [] total children | [2]
# left [20] | data [20] right | [25] total children | [5]
# left [] | data [25] right | [27] total children | [1]
# left [] | data [27] right | [] total children | [0]
# left [10] | data [15] right | [20] total children | [10]
t.print_level_order()
# ---- level order ----
# left [10] | data [15] right | [20] total children | [9]
# left [8] | data [10] right | [12] total children | [3]
# left [17] | data [20] right | [25] total children | [4]
# left [6] | data [8] right | [] total children | [1]
# left [] | data [12] right | [] total children | [0]
# left [16] | data [17] right | [] total children | [1]
# left [] | data [25] right | [27] total children | [1]
# left [] | data [6] right | [] total children | [0]
# left [] | data [16] right | [] total children | [0]
# left [] | data [27] right | [] total children | [0]
# --- END Level Order ----
