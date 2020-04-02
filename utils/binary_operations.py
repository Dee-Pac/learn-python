import math

def get_binary(num):
    """
    Converts a Number to Binary
    
    Parameters:
        num(int): The Integer
    
    Returns:
        (str): The Binary representation
    """
    base = 2
    quotient = num
    arr = ""
    while (quotient >= base):
        remainder = str(quotient%base)
        quotient = math.floor(quotient/base)
        arr+=remainder
    arr+=str(quotient)
    return str(arr[::-1])

# print(get_binary(8))
# 1000
