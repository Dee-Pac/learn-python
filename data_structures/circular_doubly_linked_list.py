class Node:
    def __init__(self,key,val,prv=None,nxt=None):
        self.key = key
        self.val = val
        self.prv = prv
        self.nxt = nxt

    def __repr__(self):
        prv_key = self.prv.key if (self.prv) else None
        prv_val = self.prv.val if (self.prv) else None
        nxt_key = self.nxt.key if (self.nxt) else None
        nxt_val = self.nxt.val if (self.nxt) else None
        return "{}.{} | {}.{} | {}.{}".format(prv_key,prv_val,self.key,self.val,nxt_key,nxt_val)

print("-----------Node-----------")
node1 = Node(1,"deepak")
print(node1)
# None.None | 1.deepak | None.None
node1.prv = node1.nxt = node1 
print(node1)
# None.None | 1.deepak | None.None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert(self,key,val):
        new_node = Node(key,val)
        if (self.head == None): # first element
            new_node.prv = new_node
            new_node.nxt = new_node
            cl.head = new_node
        else: # insert before head
            curr_prv = self.head.prv
            new_node.prv = curr_prv
            curr_prv.nxt = new_node
            new_node.nxt = self.head
            self.head.prv = new_node
        self.count+=1
        return self

    def generate_forward(self):
        ctr = 0
        while (ctr < self.count):
            to_gen = self.head
            self.head = self.head.nxt
            ctr+=1
            yield(to_gen)

    def generate_backward(self):
        ctr = 0
        while (ctr < self.count):
            to_gen = self.head
            self.head = self.head.prv
            ctr+=1
            yield(to_gen)

    def curr(self):
        return self.head

    def is_empty(self):
        return self.count == 0

    def get_count(self):
        return self.count

    def next(self):
        if (self.head == None):
            return None
        else:
            self.head = self.head.nxt
            return self.head

    def prev(self):
        if (self.head == None):
            return None
        else:
            self.head = self.head.prv
            return self.head

    def delete(self,key):
        itr = 0
        is_found = False
        while (itr<self.count):
            if (self.head.key == key):
                tmp = self.head
                prv = tmp.prv
                nxt = tmp.nxt
                prv.nxt = nxt
                nxt.prv = prv
                self.head = nxt
                print("[{}] Not Found. Deleting [{}] after iterations [{}]".format(key,tmp,itr))
                is_found=True
                self.count -= 1
                del(tmp)
            else:
                self.head = self.head.nxt
                itr+=1
        print("[{}] Not Found".format(key) if (not is_found) else "Deleted")
        return self
                
cl = CircularLinkedList()

print("----------insert------------")

print(cl.get_count(),cl.is_empty())
# (0, True)
cl.insert(1,"alpha")
print(cl.head)
# 1.alpha | 1.alpha | 1.alpha
cl.insert(2,"beta")
print(cl.head.nxt)
# 1.alpha | 2.beta | 1.alpha
cl.insert(3,"gamma").insert(4,"theta")
print(cl.head.nxt.nxt)
# 2.beta | 3.gamma | 1.alpha
print(cl.get_count(),cl.is_empty())
# (4, False)

print("----------generate_forward------------")

for i in cl.generate_forward():
    print(i)

# 4.theta | 1.alpha | 2.beta
# 1.alpha | 2.beta | 3.gamma
# 2.beta | 3.gamma | 4.theta
# 3.gamma | 4.theta | 1.alpha

print("----------generate_backward------------")

for i in cl.generate_backward():
    print(i)

# 4.theta | 1.alpha | 2.beta
# 3.gamma | 4.theta | 1.alpha
# 2.beta | 3.gamma | 4.theta
# 1.alpha | 2.beta | 3.gamma

print("----------curr/next/prev------------")

print("curr -> ",cl.curr())
print("next -> ",cl.next())
print("next -> ",cl.next())
print("curr -> ",cl.curr())
print("prev -> ",cl.prev())

# ('curr -> ', 4.theta | 1.alpha | 2.beta)
# ('next -> ', 1.alpha | 2.beta | 3.gamma)
# ('next -> ', 2.beta | 3.gamma | 4.theta)
# ('curr -> ', 2.beta | 3.gamma | 4.theta)
# ('prev -> ', 1.alpha | 2.beta | 3.gamma)

print("----------delete------------")

cl.delete(2)
# [2] Not Found. Deleting [1.alpha | 2.beta | 3.gamma] after iterations [0]
# Deleted
print(cl.get_count(),cl.is_empty())
# (3, False)
cl.delete(2)
# [2] Not Found

print("----------generate_forward------------")

for i in cl.generate_forward():
    print(i)
# 1.alpha | 3.gamma | 4.theta
# 3.gamma | 4.theta | 1.alpha
# 4.theta | 1.alpha | 3.gamma
