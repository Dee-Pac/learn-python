class Node:
    def __init__(self,key,data,prv=None, nxt = None):
        self.key = key
        self.data = data
        self.prv = prv
        self.nxt = nxt
        
    def getString(self):
        return "{}.{}".format(self.key,self.data)
        
    def __repr__(self):
        prv = self.prv.getString() if (self.prv) else ""
        nxt = self.nxt.getString() if (self.nxt) else ""
        return str("[{}] -> [{}] -> [{}]".format(prv,self.getString(),nxt))

class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
    
    def append(self,key,data):
        if (self.start):
            first = self.start
            new_node = Node(key,data, None, first)
            first.prv = new_node
            self.start = new_node
        else:
            self.start = Node(key,data)
            self.end = self.start
        return self
    
    def findByKey(self,key):
        node = self.start
        while (True):
            if (node):
                if (node.key == key):
                    return node
                else:
                    node = node.nxt
            else:
                break
                
    def updateByKey(self,key,data):
        to_update = self.findByKey(key)
        if (to_update):
            to_update.data = data 
            return self
        else:
            self.append(key,data)
            return self
                      
    def peek(self):
        return self.start
    
    def pop(self):
        if (self.start):
            start =self.start
            self.start = self.start.nxt
            return start
        else:
            return None

    def deleteByKey(self,key):
        node = self.start
        while (True):
            if (node == None):
                break
            elif (node.key == key):
                to_delete = node
                if (to_delete.prv != None): to_delete.prv.nxt = to_delete.nxt
                if (to_delete.nxt !=None): to_delete.nxt.prv = to_delete.prv
                del to_delete
                break
            else:
                node = node.nxt

    
    def getLast(self):
        return self.end
    
    def __repr__(self):
        counter = 0
        node = self.start
        nodes_str = ""
        while (True):
            if (node == None):
                break
            else:
                counter +=1
                nodes_str += "[{}] ".format(node.getString())
                node = node.nxt
        return str(counter) + " | " + nodes_str
    
    def length(self):
        counter = 0
        node = self.start
        while (True):
            if (node == None):
                break
            else:
                counter +=1
                node = node.nxt
        return counter


class HashMap:
    def __init__(self,buckets = 2**10):
        self.buckets = buckets
        self.array = [None]*self.buckets
        
    def hash(self,key):
        return key%self.buckets
    
    def put(self,key,data):
        bucket = self.hash(key)
        bucket_data = self.array[bucket]
        if (not bucket_data):
            lst = LinkedList()
            lst.append(key,data)
            self.array[bucket] = lst
        else:
            self.array[bucket].updateByKey(key,data)
        return self
    
    def get(self,key):
        bucket = self.hash(key)
        bucket_data = self.array[bucket]
        if (bucket_data == None):
            return None ## if the list at index is empty, return None
        else:
            node = bucket_data.findByKey(key)
            if (node): ## if the key is found in the list, return data
                data = node.data
            else:
                data = None
        return data 
    
    def length(self):
        index = 0
        ctr = 0
        while (index < self.buckets):
            if (self.array[index] == None):
                pass
            else:
                l = self.array[index]
                ctr += l.length()
            index +=1
        return ctr
    
        
map = HashMap()
for k in range(0,130):
    map.put(k,chr(k))
for k in range(0,130):
    print(str(k),map.get(k))
print(map.get(65))
#A
map.put(65,"x")
print(map.get(65))
#x
print(map.length())
#130



