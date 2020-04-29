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
    

