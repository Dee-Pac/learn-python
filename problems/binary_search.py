
# -- Simple Binary Search of sorted array

def find(nums, num):
    
    size = len(nums)
    start = 0
    end = size - 1
    
    found = None
    
    while (start <= end):
        
        offset = (end - start)//2
        middle = start + offset
        
        if ( nums[middle] == num ):
            found = middle
            break
        else:
            if ( num > nums[middle] ):
                start = middle + 1
            else:
                end = middle - 1
        
    if (found):
        print(found)
    else:
        print("Not Found")
        
    
# find([1,2,3,4,5,6],10)


# -- Find First or last index of an element

nums = [2, 3, 10, 10, 10, 10, 18, 20]

def findFirstOrLastIter(nums, num, first = True):
    
    result = None
    
    size = len(nums)
    start = 0
    end = size - 1
    
    
    while (start <= end):
        
        offset = (end - start) // 2
        middle = start + offset
        
        if (num == nums[middle]):
            result = middle
            if (first): end = middle - 1
            else: start = middle + 1
        elif (num < nums[middle]):
            end = middle - 1
        else:
            start = middle + 1
    
    return result

# print(findFirstOrLastIter(nums, 10))
# print(findFirstOrLastIter(nums, 200))
# print(findFirstOrLastIter(nums, 3))
# print(findFirstOrLastIter([], 2))
# print(findFirstOrLastIter(nums, 2))
# print(findFirstOrLastIter(nums, 20))


# -- FIND ALL OCURRENCES OF AN ELEMENT

def findAll(nums, num):
    
    first = findFirstOrLastIter(nums, num)
    last = findFirstOrLastIter(nums, num, False)
    
    return (first, last)

    
print(findAll(nums, 3))
print(findAll(nums, 10))
print(findAll([10,10], 10))





# -- Given sorted array that is rotated, find how many times rotated
# -- Solution : the middle is the lowest & its index is the rotated times.

def howManyRotated(nums):
    
    size = len(nums)
    start = 0
    end = size-1
    
    while (start <= end):
        
        offset = (end-start) // 2
        middle = start + offset
        # print(start, middle, end, middle+1)
        if (nums[middle] > nums[end]):
            # print("a")
            start = middle + 1
        elif (nums[start] > nums[middle - 1]):
            # print("b")
            end = middle - 1
        else:
            break
            
    print(middle)
    
nums1 = [3,4,5, 1,2]
nums2 = [6,1,2,3,4,5]
nums3 = [6,7,8,9,1,2,3,4,5]

        
# howManyRotated(nums1)
# howManyRotated(nums2)
# howManyRotated(nums3)

                
def findElementInSortedRotatedArray(nums, num):
    
    size = len(nums)
    end = size - 1
    start = 0
    
    while (start <= end):
        
        offset = (end-start)//2
        middle = start + offset
        
        # print(start, end, middle)
        
        if (num == nums[middle]):
            return middle
        
        isLeftSorted = nums[start] <= nums[middle-1]
        isRightSorted = nums[middle+1] <= nums[end]
        isNumInLeftRange = num >= nums[start] and num <= nums[middle-1]
        isNumInRightRange = num >= nums[middle+1] and num <= nums[end]  
        
        if (isLeftSorted):
            if isNumInLeftRange:
                end = middle-1
            else:
                start = middle+1
        else:
            if isNumInRightRange:
                start = middle+1
            else:
                end= middle-1

        # print(start, end, middle)
            
    return -1

# print(findElementInSortedRotatedArray([6,1,2,3,4,5],4))
# print(findElementInSortedRotatedArray([6,1,2,3,4,5],1))
# print(findElementInSortedRotatedArray([6,7,8,9,1],1))                

            


