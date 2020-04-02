
def sum(l,acc=0):
    """
    Returns the sum of integers
    
    Parameters:
        l(list) : List of integers
    Returns:
        (integer) : the sum of list of integers
    """

    l = list(l)
    if(l):
        val = l.pop()
        acc += val
        return sum(l,acc)
    else:
        return acc

def mul(l,acc=1):
    """
    Returns the product of integers
    
    Parameters:
        l(list) : List of integers
    Returns:
        (integer) : the product of list of integers
    """

    l = list(l)
    if(l):
        item = l.pop()
        acc*=item
        return (mul(l,acc))
    else:
        return acc

#print(sum([1,2,3,4]))
#10
#print(mul([1,2,3,4]))
#24
