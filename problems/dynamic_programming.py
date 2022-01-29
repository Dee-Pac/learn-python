def fib(n, d= {}):
    
    if (n in d):
        return d[n]
    
    if n <=1:
        return n
    
    d[n] = fib(n-2, d) + fib(n-1, d)
    return d[n]

# print(fib(50))


def gridTravel(m,n, d = {}):
    
    key = "{}_{}".format(m,n)
    
    if key in d:
        return d[key]
    
    if (m < 1 or n < 1):
        return 0
    
    if (m,n) == (1,1):
        return 1
    
    d[key] = gridTravel(m-1, n, d) + gridTravel(m, n-1, d)
    return d[key]

# print(gridTravel(4,4))


def canSum(num, nums, d = dict()):
    
    # print(num)
    if num in d:
        return d[num]
    
    if (num == 0):
        return True
    if (num < 0):
        return False
    
    for n in nums:
        
        d[num-n] = canSum(num-n, nums, d)
        if (d[num-n]):
            return True
        
    return False
    
    

# print(canSum(2001, [2, 4, 6, 8]))




def howSum(num, nums, d = {}):
    
    if num in d:
        return d[num]
    
    if (num == 0):
        return []
    
    if (num < 0):
        return None
    
    for n in nums:
        
        newNum = num - n
        d[num] = howSum(newNum, nums)
        if d[num] != None:
            d[num].append(n)
            return d[num]
            
    return None

# print(howSum(300, ([7,4])))
# print(howSum(2001, [2, 4, 6, 8]))




def bestSum(num, nums, d = dict()):
    
    
    if num in d:
        return d[num]
    
    if (num == 0):
        return []
    
    if (num < 0):
        return None
    
    shortest = None
    
    for n in nums:
        
        newNum = num - n
        d[newNum] = bestSum(newNum, nums, d)
        if d[newNum] != None:
            res = d[newNum] + [n]
            if shortest == None or (len(res) < len(shortest)):
                shortest = res
            
    d[num] = shortest
    return shortest

# print(bestSum(7, [5,3,4,7], {}))
# print(bestSum(8, [1,2,3,5], {}))

# print(bestSum(8, [1,4,5], {})) 
# print(bestSum(100, [1,2,5,25], {}))


def canConstruct(target:str, strings:list[str], d = dict()):

    
    if target in d:
        return d[target]
    
    if (len(target) == 0):
        return True
    
    for string in strings:
        
        if (target.startswith(string)):
            newTarget = target[len(string):]
            d[newTarget] = canConstruct(newTarget, strings, d)
            return d[newTarget]
        
    return False

# print(canConstruct("abcd", ["a", "bc", "cd"], {}))
# print(canConstruct("abcd", ["a", "bc", "cd", "d"], {}))
# print(canConstruct("eeeeeeeeeeeeeeeeeeeeeef", ["e", "eeee", "f"], {}))

    

def countConstruct(target:str, strings:list[str], d = dict()):
    
    if target in d:
        return d[target]
    
    if (len(target) == 0):
        return 1
    
    count = 0
    
    for string in strings:
        
        if (target.startswith(string)):
            newTarget = target[len(string):]
            res = countConstruct(newTarget, strings, d)
            count += res
    
    d[target] = count
    return count

def anyConstruct(target:str, wordBank:list[str], d= dict()):
    
    # print(target, d)
    
    if target in d:
        return d[target]
    
    if (len(target) == 0):
        return []
    
    result = None
    for word in wordBank:
        
        if (target.startswith(word)):
            suffix = target[len(word):]
            suffixWays = anyConstruct(suffix, wordBank, d)
            if (suffixWays is not None):
                suffixWays.append(word)
                result = suffixWays
                
    return result

# print(anyConstruct("abc", ["a","b","c","abc", "a", "bc"], {}))
    

# print(countConstruct("abcde", ["abc","de","a", "b", "bc", "cd", "e", "abcad", "abcde", "abcde"], {}))
# print(countConstruct("aaaaaaaaaaaaa", ["a", "aa", "b", "bc", "cd", "e", "abcad", "abcde", "abcde"], {}))



def allConstruct(target:str, wordBank:list[str], d= dict()):
    
    if target in d:
        return d[target]
    
    if (len(target) == 0):
        return [[]]
    
    result = []
    
    for word in wordBank:
        
        if (target.startswith(word)):
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank, d) 
            if suffixWays is not None:
                for siffixWay in suffixWays:
                    siffixWay.append(word)
                    result.append(siffixWay)
                    
    d[target] = result
                    
    return result


# print(allConstruct("abc", ["a","b","c","abc", "bc"], {}))
# print(allConstruct("purple", ["pur", "pl", "p", "l", "e", "le", "ple"], {}))
# print(allConstruct("aaaaaaaaaaaaaaaaaaaaaaazk", ["aa","a","aaaa","z"], {}))



