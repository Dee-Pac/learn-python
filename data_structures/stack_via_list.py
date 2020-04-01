class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
        return self
        
    def pop(self):
        item = self.items.pop(-1)
        return item
        
    def peek(self):
        return self.items[-1]
    
    def __repr__(self):
        return str(self.items)
        
stack = Stack()
stack.push(1).push(2).push(3)
print(stack.pop(),stack)
# 3 [1, 2]
print(stack.pop(),stack)
# 2 [1]
print(stack.peek())
# 1

