class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return "[Data --> {} | next --> {}]".format(self.data,self.next)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __repr__(self):
        return "head --> {} \ntail --> {}".format(self.head,self.tail)
    
    def append(self,data):
        node = Node(data)
        if (not self.head):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        return self

    def prepend(self,data):
        if (not self.head):
            node = Node(data)
            self.head = node
            self.tail = node
        else:
            node = Node(data,self.head)
            self.head = node
        return self
    
    def is_exists(self,data):
        is_found = False
        index = 0
        node = self.head
        while (node):
            # print(node)
            if (node.data == data):
                # print("Found [{}]at index position [{}]".format(data,index))
                is_found = True
                break
            else:
                node = node.next
                index+=1
        print("<is_exists> Found [{}] at index position [{}]".format(data,index) if is_found else "[{}] Not Found after checking [{}] elements.".format(data,index))
        return is_found
            
        
    def swap(self,data1,data2):
        if (not self.head):
            print("List Empty, Nothing swapped!")
        elif (self.head == self.tail):
            print("Only one element in the list, Nothing swapped!")
        elif (data1 == data2):
            print("Inputs are the same, Nothing swapped!")
        elif (not self.is_exists(data1)):
            print("[{}] does not exist in the list, Nothing swapped!".format(data1))
        elif (not self.is_exists(data2)):
            print("[{}] does not exist in the list, Nothing swapped!".format(data2))
        else:
            print("catchall")
            node = self.head
            prev_node = None
            prev_node1 = None
            node1 = None
            prev_node2 = None
            node2 = None
            print("begin locating..")
            while (node):
                if (node.data == data1):
                    prev_node1 = prev_node
                    node1 = node
                elif (node.data == data2):
                    prev_node2 = prev_node
                    node2 = node
                else:
                    pass
                prev_node = node
                node = node.next
                    
                if (node1 and node2):
                    print("found both")
                    break # break the loop if both elements are found
                
            print("begin swapping..")
            if (self.head == node1):
                print("not assigning for head element [{}]".format(node1.data))
                self.head = node2
                prev_node2.next = node1
            elif (self.head == node2):
                print("not assigning for head element [{}]".format(node2.data))
                self.head = node1
                prev_node1.next = node2
            else:
                "Head not impacted by swap"
                prev_node1.next = node2
                prev_node2.next = node1
            tmp = node2.next
            node2.next = node1.next
            node1.next = tmp
        return(self)
    

list = LinkedList()
print(list.append(1).append(2).prepend(0).prepend(-1))
# head --> [Data --> -1 | next --> [Data --> 0 | next --> [Data --> 1 | next --> [Data --> 2 | next --> None]]]] 
# tail --> [Data --> 2 | next --> None]
list.is_exists(3)
# [3] Not Found after checking [4] elements.
list.is_exists(1)
# <is_exists> Found [1] at index position [2]
list.swap(1,1)
# Inputs are the same, Nothing swapped!
list.swap(1,4)
# <is_exists> Found [1] at index position [2]
# [4] Not Found after checking [4] elements.
# [4] does not exist in the list, Nothing swapped!
print(list.swap(1,-1))
# <is_exists> Found [1] at index position [2]
# <is_exists> Found [-1] at index position [0]
# catchall
# begin locating..
# found both
# begin swapping..
# not assigning for head element [-1]
# head --> [Data --> 1 | next --> [Data --> 0 | next --> [Data --> -1 | next --> [Data --> 2 | next --> None]]]] 
# tail --> [Data --> 2 | next --> None]
