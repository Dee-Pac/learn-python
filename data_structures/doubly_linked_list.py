class Node:
    """
    Holds the key value pairs
    """
    
    def __init__(self,key,data,prv=None,nxt=None):
        self.key = key
        self.data = data
        self.prv = prv
        self.nxt = nxt
        
    def __repr__(self):
        prv_data = "{}.{}".format(self.prv.key,self.prv.data) if (self.prv != None) else None
        nxt_data = "{}.{}".format(self.nxt.key,self.nxt.data) if (self.nxt != None) else None
        return str("[ {} <- {}.{} <- {} ]".format(prv_data,self.key,self.data,nxt_data))
    
class LinkedList:
    
    """
    Doubly Linked List
    """
    
    def __init__(self):
        self.start = None
        self.end = None
    
    def append(self,key,data):
        if (self.start == None):
            new_node = Node(key,data)
            self.start = new_node
            self.end = new_node
        else:
            new_node = Node(key,data,prv = None, nxt = self.start)
            self.start.prv = new_node
            self.start = new_node
        return self

    def updateByKey(self,key,data):
        if (self.start ==None):
            pass
        else:
            node = self.start
            while (node):
                if (node.key == key):
                    node.data = data
                    break
                node=node.nxt
        return self
        
    def length(self):
        if (self.start == None):
            return 0
        else:
            node = self.start
            ctr=0
            while (node):
                node = node.nxt
                ctr+=1
            return ctr
        
    def findByKey(self,key):
        if (self.start == None):
            return None
        else:
            node = self.start
            while (True):
                if (node.key == key):
                    return node.data
                else:
                    if (node.nxt == None):
                        break
                    node = node.nxt   
    
    def findPrevByKey(self,key):
        if (self.start == None):
            return None
        else:
            node = self.start
            while (True):
                if (node.key == key):
                    return node.prv
                else:
                    if (node.nxt == None):
                        break
                    node = node.nxt
                    
    def findNextByKey(self,key):
        if (self.start == None):
            return None
        else:
            node = self.start
            while (True):
                if (node.key == key):
                    return node.nxt
                else:
                    if (node.nxt == None):
                        break
                    node = node.nxt
                    
    def __repr__(self):
        lst = ""
        if (self.start == None):
            pass
        else:
            node = self.start
            ctr=0
            while (node):
                lst += "{} : {} | ".format(ctr,node)
                node = node.nxt
                ctr+=1
        return lst


lst = LinkedList()

lst.append(1,"a").append(2,"x").append(3,"b").append(4,"k")

print(lst)
# 0 : [ None <- 4.k <- 3.b ] | 1 : [ 4.k <- 3.b <- 2.x ] | 2 : [ 3.b <- 2.x <- 1.a ] | 3 : [ 2.x <- 1.a <- None ] | 
print(lst.length())
# 4
print(lst.findByKey(4))
# k
print(lst.findPrevByKey(2))
# [ 4.k <- 3.b <- 2.x ]
print(lst.findNextByKey(4))
# [ 4.k <- 3.b <- 2.x ]
print(lst.updateByKey(4,"k1"))
# 0 : [ None <- 4.k1 <- 3.b ] | 1 : [ 4.k1 <- 3.b <- 2.x ] | 2 : [ 3.b <- 2.x <- 1.a ] | 3 : [ 2.x <- 1.a <- None ] | 
