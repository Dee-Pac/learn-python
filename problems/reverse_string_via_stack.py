import sys
sys.path.append('/Users/dmohanakumarchan/workspace/eclipse_luna/learn-python/data_structures')

from stack_via_list import Stack

def reverse_string(str):
    stack = Stack()
    reversed = ""
    for char in str:
        stack.push(char)
    while(not stack.is_empty()):
        reversed += stack.pop()
    return reversed

print(reverse_string("hello"))
# olleh
