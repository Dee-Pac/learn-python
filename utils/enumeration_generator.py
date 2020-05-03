def gen_seq(lst,start=0):
    """Generates Sequence

        Parameters:
            lst(list): a list of items
            start(int): the starting value of the sequence, default = 0
        Returns:
            list: list if tuples [(seq,original_item_in_list)]
    """
    i = 0
    for item in lst:
        i+=1
        yield i,item

# Input List

l = list(["a","b","c","d"])

# Out of the box - enumeration
for item in enumerate(l,1):
    print(item)
    
# Custom Enumeration
for items in gen_seq(l,1):
    print(type(items),items)    
    
items = gen_seq(l,1)

print(next(items))
# (1, 'a')
print(next(items))
# (2, 'b')
print(next(items))
# (3, 'c')
print(next(items))
# (4, 'd')
# print(next(items))
# Traceback (most recent call last):
#   File "/Users/dmohanakumarchan/workspace/eclipse_luna/learn-python/test.py", line 25, in <module>
#     print(next(items))
# StopIteration

i= [1,2,3]
# square each term using list comprehension
l = [x**2 for x in i]
# same thing can be done using generator expression
g = (x**2 for x in l)
print(l)
# [1, 4, 9]
print(g)
# <generator object <genexpr> at 0x10eadf960>
print(next(g))
# 1
print(next(g))
# 16

# More https://www.programiz.com/python-programming/generator


