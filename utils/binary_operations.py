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

import math
def get_int(bin_string):
    base = 2
    res = 0
    for bit in enumerate(bin_string[::-1]):
        bit_position = bit[0]
        bit_value = bit[1]
        print(bit_position,bit_value)
        res += int(math.pow(base,bit_position)) * int(bit_value)
    return res

print(get_int("1000"))
# 0 0
# 1 0
# 2 0
# 3 1
# 8

print(get_int("0111"))
# 0 1
# 1 1
# 2 1
# 3 0
# 7
