
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



def reverseString(s):
    
    print(s)
    if (not s):
        return ""
    
    if (len(s) == 1):
        return s[0]
    else:
        return reverseString(s[1:]) + s[0] 
    
# print(reverseString("recursion"))


def isPalindrome(s, start = None, end = None):
    
    
    start = 0 if not start else start
    end = len(s) - 1 if not end else end
    print(s[start:end+1])
    
    if (start >= end): 
        return True
    
    if (s[start] == s[end]):
        return isPalindrome(s, start+1, end-1)
    else:
        return False
    
# print(isPalindrome("1kayyak1"))
# print(isPalindrome("1kayak1"))

def isPalindrome(s):
    
    print(s)
    if (len(s) <= 1): 
        return True
    
    if (s[0] == s[len(s)-1]):
        return isPalindrome(s[1:len(s)-1])
    else:
        return False


# print(isPalindrome("1kayyak1"))
# print(isPalindrome("1kayak1"))


def binaryOf(num):
    
    
    q = num // 2
    r = num % 2
    print(num, q, r)
    if q == 0:
        return str(r)
    else: 
        return binaryOf(q) + str(r)

# print(binaryOf(3))


def sumNatural(num):
    
    if num == 1:
        return 1
    else:
        return num + sumNatural(num-1)
    
# print(sumNatural(10))


# import time


def binarySearch(arr, num, s = None, e = None):
    
    # time.sleep(0.1)
    
    s = 0 if not s else s
    e = len(arr) - 1 if not e else e
    middle = (s+e) // 2
    print(arr[s:e], s, e, middle)
    
    if (s > e):
        return -1
    
    if (arr[middle] == num):
        return middle
    
    if (num < arr[middle]):
        return binarySearch(arr, num, s, middle-1)
    else:
        return binarySearch(arr, num, middle+1, e)
    
    
    
# print(binarySearch([-1, 10, 20, 33, 41,43], 20))


def fib(n, d = dict()):
    
    if n in d:
        return d[n]
    
    if n <=1:
        return n
    
    d[n]=  fib(n-2) + fib(n-1)
    return d[n]

# print(fib(50))

def merge(a, b):
    
    e1 = len(a)-1
    e2 = len(b)-1
    s1 = 0
    s2 = 0
    
    result = []
    
    while (s1 <= e1 and s2 <= e2):
        if a[s1] <= b[s2]:
            result.append(a[s1])
            s1+=1
        else:
            result.append(b[s2])
            s2+=1
    
        
    while s1 <= e1:
        result.append(a[s1])
        s1+=1
        
    while s2 <= e2:
        result.append(b[s2])
        s2+=1
    
    return result

# print(merge([30], [20]))
        

def mergeSort(nums):
    
    if (len(nums) <= 1):
        return nums
    
    middle = len(nums) // 2
    left = nums[0:middle]
    right = nums[middle:]
    
    return merge(mergeSort(left), mergeSort(right))

import random
num2 = list(range(1,30,3))
random.shuffle(num2)
print(num2)
print(mergeSort(num2))

def mergeSort(nums, s = None, e = None):
    
    if (len(nums) <= 1):
        return nums
    
    s = 0 if not s else s
    e = len(nums) - 1 if not e else e
    m = (s+e)//2
    
    return merge(mergeSort(nums,s,m), mergeSort(nums,m+1,e))

import random
num2 = list(range(1,30,3))
random.shuffle(num2)
print(num2)
print(mergeSort(num2))


    
    
    



