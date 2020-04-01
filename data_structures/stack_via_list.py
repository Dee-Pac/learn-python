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
    
    def length(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items == []
    
    def __repr__(self):
        return str(self.items)
        
# stack = Stack()
# stack.push(1).push(2).push(3)
# print("Popped -> {} | Stack -> {} | Length -> {} | Empty? -> {}".format(stack.pop(),stack, stack.length(), stack.is_empty()))
# 3 [1, 2]
# print("Popped -> {} | Stack -> {} | Length -> {} | Empty? -> {}".format(stack.pop(),stack, stack.length(), stack.is_empty()))
# 2 [1]
# print(stack.peek())
# 1

