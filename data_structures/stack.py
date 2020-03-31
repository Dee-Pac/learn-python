class Node:
    """Represents the Element in a list"""

    def __init__(self,i,next=None):
        self.i=i # Assign data
        self.next=next # link the previous node
    def __repr__(self): 
        return "[Data : {} | Next -> {}]".format(self.i,self.next)

class Stack:
    """Represents the Stack"""

    def __init__(self):
        self.head=None

    def push(self,i):
        """
        Push Operation for the Stack

        Parameters:
            i (int): Data

        Returns:
            Stack: The stack resulting from the push operation
        """
        print("request to push {}".format(i))
        if (self.head == None):
            print("head is empty")
            self.head = Node(i)  # initiate the list
        else:
            print("head is {}".format(self.head))
            new_node = Node(i,self.head)
            print("new node | {}".format(new_node))
            self.head = new_node
        return self
    
    def pop(self):
        """
        Pop Operation for the Stack

        Parameters:
            
        Returns:
            Node: The data from the top of the stack
        """
        if (self.head == None):
            return None
        else:
            node = self.head
            self.head = self.head.next # release head & assign next node as head
            return node # return head
    
    def is_empty(self):
        """
        Check if the stack is empty

        Parameters:
            
        Returns:
            Boolean: True if stack is Empty | False if stack is NOT Emtpy
        """
        return self.head==None

    def length(self):
        """
        Find the length of the Stack

        Parameters:
            
        Returns:
            int: Length of the stack
        """
        if (self.is_empty()):
            return 0 # base case - empty list
        else:
            each_node = self.head
            i =1
            while (each_node.next):
                i+=1
                each_node = each_node.next
            return i

    def find_first(self,i):
        """
        Find the first ocurrence of an element in the stack

        Parameters:
            i (int): Element to be searched
        Returns:
            Node: The Node containing the element
            string: A Message with more details
        """
        ix=1
        each_node=self.head
        is_found=False
        while(each_node.next): # iterate until the end of list is reached
            if (each_node.i==i):
                is_found=True
                break # break loop if data is found
            else:
                ix+=1
            each_node=each_node.next
        return each_node,"Found {} at index {}".format(i,ix) if is_found else "{} Not Found in all of {} elements".format(i,ix)
    
    def find_by_index(self,index):
        """
        Returns the element in the specified index

        Parameters:
            index (int): The position of data being requested
        Returns:
            Node: The Node containing the element
        """
        if (self.length()<index+1): 
            print("Stack is Empty")
            return None
        else:
            counter = 0
            each_node =self.head
            while(each_node.next):
                if (counter == index):
                    break
                else:
                    counter+=1
                    each_node = each_node.next
            return each_node

    def __repr__(self):
        return(str(self.head))


stack = Stack()
print("Stack Length -> {}".format(stack.length()))
# Stack Length -> 0
stack.push(10)
# request to push 10
# head is empty
stack.push(20)
# request to push 20
# head is [Data : 10 | Next -> None]
# new node | [Data : 20 | Next -> [Data : 10 | Next -> None]]
stack.push(30)
# request to push 30
# head is [Data : 20 | Next -> [Data : 10 | Next -> None]]
# new node | [Data : 30 | Next -> [Data : 20 | Next -> [Data : 10 | Next -> None]]]
print(stack.find_by_index(10))
# None
print(stack.find_first(2))
# None
# ([Data : 10 | Next -> None], '2 Not Found in all of 3 elements')
print(stack.find_first(20))
# ([Data : 20 | Next -> [Data : 10 | Next -> None]], 'Found 20 at index 2')


