print("+++++++++++++++++++++++++++++++++++++")
print("------Randomize------")
print("+++++++++++++++++++++++++++++++++++++")

import random
l = list(range(1,10))
random.shuffle(l)
print(l)

print("+++++++++++++++++++++++++++++++++++++")
print("------Sample------")
print("+++++++++++++++++++++++++++++++++++++")

sample = random.sample(l,3)
print(sample,l)

print("+++++++++++++++++++++++++++++++++++++")
print("------Hash function------")
print("+++++++++++++++++++++++++++++++++++++")

import hashlib

h_func = hashlib.sha512()
h_func.update(b"plain_text_data")
hexval = h_func.hexdigest()
intval = int(hexval,16)
two_digit_hash = intval % 10**2
print("hexval [{}] intval [{}] 2_digit [{}]".format(hexval,intval,two_digit_hash))

print("+++++++++++++++++++++++++++++++++++++")
print("------Remove Duplicates------")
print("+++++++++++++++++++++++++++++++++++++")

l1 = list(range(1,3)) + list(range(1,5))
print(l1,list(set(l1)))

print("+++++++++++++++++++++++++++++++++++++")
print("------if list has same entry------")
print("+++++++++++++++++++++++++++++++++++++")

from collections import Counter
Counter(l1)
l2 = list([1, 2, 4, 2, 3,1])
print(Counter(l1)==Counter(l2))

print("+++++++++++++++++++++++++++++++++++++")
print("------Dictionary merge------")
print("+++++++++++++++++++++++++++++++++++++")

keys = [1,2,3,4]
values = ["a","b","c","d"]

kv_pairs = zip(keys,values)
print(kv_pairs)
d1 = dict(kv_pairs)
print(d1)
d2 = {10:"deepak"}
d1.update(d2)
print(d1)

print("+++++++++++++++++++++++++++++++++++++")
print("------Dictionary to List------")
print("+++++++++++++++++++++++++++++++++++++")

print(list(d1.items()))

print("+++++++++++++++++++++++++++++++++++++")
print("------List operations------")
print("+++++++++++++++++++++++++++++++++++++")

## reverse iterate
l = range(1,21)
for i in l[::-1]:
    print(i)
print("first {} and last {}".format(l[0],l[-1]))

slices = list()
c = 0
while (c <len(l)-1):
    slices.append((l[c],l[c+1]))
    c+=1

print("slices --> {}".format(slices))

print("+++++++++++++++++++++++++++++++++++++")
print("--------Exception handling------------")
print("+++++++++++++++++++++++++++++++++++++")
import sys
try:
    "a" +1
except:
    e = sys.exc_info()
    print(e)
finally:
    pass
    
print("+++++++++++++++++++++++++++++++++++++")
print(" ---- Map  -----")
print("+++++++++++++++++++++++++++++++++++++")

for i in map(lambda x: x+1,l):
    print(i)
    
print("+++++++++++++++++++++++++++++++++++++")
print(" ---- reduce  -----")
print("+++++++++++++++++++++++++++++++++++++")

import functools
print(functools.reduce(lambda a,b:a+b, l))

print("+++++++++++++++++++++++++++++++++++++")
print(" ---- itertools  -----")
print("+++++++++++++++++++++++++++++++++++++")

import itertools

print("+++++++++++++++++++++++++++++++++++++")
print(" ---- permutations  -----")
print("+++++++++++++++++++++++++++++++++++++")

for i in itertools.permutations(range(0,3),2):
    print(i)
    
print("+++++++++++++++++++++++++++++++++++++")
print(" ---- combinations  -----")
print("+++++++++++++++++++++++++++++++++++++")

for i in itertools.combinations(range(0,3),2):
    print(i)

print("+++++++++++++++++++++++++++++++++++++")
print(" ---- product  -----")
print("+++++++++++++++++++++++++++++++++++++")

for i in itertools.product(range(0,3),repeat=3):
    print(i)
    
print("+++++++++++++++++++++++++++++++++++++")
print(" ---- accumulate  -----")
print("+++++++++++++++++++++++++++++++++++++")

import operator
l = range(1,5)
for i in itertools.accumulate(l,operator.mul):
    print(i)

    
print("+++++++++++++++++++++++++++++++++++++")
print(" ---- URL / CURL RESPONSE  -----")
print("+++++++++++++++++++++++++++++++++++++")

import requests

URL = "https://api.github.com/users/Dee-Pac/repos"
PARAMS = {'id':1212}
PARAMS = {}
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS, verify = False)
# extracting data in json format
data = r.json()
import json
print(json.dumps(data))



print("+++++++++++++++++++++++++++++++++++++")
print(" ---- FILE HANDLER  -----")
print("+++++++++++++++++++++++++++++++++++++")


# https://www.techbeamers.com/python-file-handling-tutorial-beginners/

print("----With Auto-closes the file, at the end of operation----\n")
print("----Process line by line----\n")
with open("/Users/dmohanakumarchan/code/GEM/neo4j/import/pc_storage.csv","r") as fp:
    for line in fp:
        print(line)

print("----Process all lines at once----\n")
with open("/Users/dmohanakumarchan/code/GEM/neo4j/import/pc_storage.csv","r") as fp:
    lines = fp.readlines()
    for num,line in enumerate(lines):
        print(num,line)

writer  = open("/tmp/testing.out","w")

print("----Process few chars each time----\n")
fp =  open("/Users/dmohanakumarchan/code/GEM/neo4j/import/pc_storage.csv","r")
print("----Read 10 chars----\n")
print(fp.read(10))
print(fp.tell())
print("----Read 10 chars----\n")
print(fp.readline(10))
print(fp.tell())
fp.seek(0)
print("----Read entire file as string----\n")
data_string = fp.read()
fp.seek(0)
print("----Read entire file as list of lines----\n")
lines = fp.readlines()
print(type(data_string),type(lines))
fp.close()
writer.write(data_string + "\n")
writer.writelines(lines)
writer.close()


print("+++++++++++++++++++++++++++++++++++++")
print(" ---- CLASS INHERITENCE  -----")
print("+++++++++++++++++++++++++++++++++++++")

import json

class Window:
    def __init__(self,window_l,window_h):
        self.w_length = window_l
        self.w_height = window_h
        
    def __repr__(self):
        return json.dumps(self.__dict__)
    

class Door:
    def __init__(self,door_l,door_h):
        self.length = door_l
        self.height = door_h
        
    def __repr__(self):
        return json.dumps(self.__dict__)

class House(Window,Door):
    def __init__(self,address,window_l,window_h,door_l,door_h):
        Window.__init__(self,window_l,window_h)
        Door.__init__(self,door_l,door_h)
        self.address = address
        
    def __repr__(self):
        return json.dumps(self.__dict__)



my_house = House("california",300,100,250,200)
print(my_house)

print("+++++++++++++++++++++++++++++++++++++")
print(" ---- JSON  -----")
print("+++++++++++++++++++++++++++++++++++++")

import json,requests

# Request from URL
data = requests.get("https://api.github.com/users/Dee-Pac/repos",params = {},verify = False)
# Get dictionary
dict_data = data.json()
# Convert dict to JSON
json_data = json.dumps(dict_data)
# convert JSON to dict
d_data = json.loads("""{"id":1,"name":"deepak"}""")
print(d_data)

fp = open("/tmp/github_repo.json","w")
fp.write(json_data + "\n")
fp.close()

fp = open("/tmp/github_repo.json","r")
# load json file as dict
k = json.load(fp)
print(k)
fp.close()

print("+++++++++++++++++++++++++++++++++++++")
print(" ---- THREADING , LOCK, RE-ENTRANT LOCK  -----")
print("+++++++++++++++++++++++++++++++++++++")

from threading import Lock,Thread,current_thread
import threading

class Counter:
    def __init__(self,counter=0):
        self.counter = counter
        self.lock = Lock()

    def count(self):
        with self.lock:
            # self.lock.acquire() # Alternate for with lock:
            print(current_thread().getName(),self.counter)
            for k in range(100000):
                self.counter +=1
            # self.lock.release()

# initiate counter object
obj = Counter()

# initiate threads
threads = []

# create 40 threads for count function
for k in range(40):
    new_thread = Thread(target = obj.count,args = ())
    threads.append(new_thread)

# start the threads
for thread in threads:
    thread.start()

# wait for completion of all threads
for thread in threads:
    thread.join()

# Without above join calls, the print could execute even before all the counter functions completed.
print(obj.counter)

###---------------------- RE-ENTRANT CODE ----------------------###

# A Re-entrant code is fully atomic in the sense - it does not modify any object outside of its scope.

def pow(num):
    return num*num

# Non Re-entrant code
# Not thread safe without an explicit lock
k = 10
def pow1(num):
    global k 
    k +=1
    return num*num

###---------------------- RE-ENTRANT LOCK ----------------------###

# Ability of a thread to re-acquire lock in something it already had (locked)

from threading import *

lock = Lock()
k = lock.acquire()
print("first locked {}".format(k))
k = lock.acquire(timeout=0)
print("second locked {}".format(k))
lock.release()

# first locked True
# second locked False

from threading import *

lock = RLock()
k = lock.acquire()
print("first locked {}".format(k))
k = lock.acquire()
print("second locked {}".format(k))
lock.release()

# first locked True
# second locked True

## Regex

print("+++++++++++++++++++++++++++++++++++++")
print(" ---- URL Parsing  -----")
print("+++++++++++++++++++++++++++++++++++++")

import urllib

str = "https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-1.5"

url = urllib.parse.urlparse(str)
print(url)

str1 = urllib.parse.urlunparse(url)
print(str1)


print("+++++++++++++++++++++++++++++++++++++")
print(" ---- TIME & DATE  -----")
print("+++++++++++++++++++++++++++++++++++++")

import time, datetime

# ---- TIME Difference ----

t1 = time.time()
time.sleep(2)
t2 = time.time()

print("difference seconds {}".format(t2-t1))

# ---- DATE Difference ----

# finding time difference
date1 = datetime.datetime.strptime("2020-12-31 00:00:00","%Y-%m-%d %H:%M:%S")
date2 = datetime.datetime.strptime("2021-12-31 00:00:00","%Y-%m-%d %H:%M:%S")
time_delta = date2-date1

# adding time to dates
time_delta = datetime.timedelta(hours=-48)
new_date = date1 + time_delta
print("old date [{}] with delta [{}] = new date [{}]".format(date1,time_delta,new_date))
print(str(date2))


print("+++++++++++++++++++++++++++++++++++++")
print(" ---- DATABASE  -----")
print("+++++++++++++++++++++++++++++++++++++")

## ---- MYSQL ---- 

import mysql.connector
import sys

class SQLConnector:
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connector = mysql.connector

    def executeSQL(self,sqlText):
        con = self.connector.connect(host = self.host,user = self.user,password = self.password,database = self.database)
        result = None
        try:
            cursor = con.cursor()
            cursor.execute(sqlText)
            result = cursor.fetchall()
        except:
            e = sys.exc_info()
            print(e)
        finally:
            con.close()
        return result

mysql = SQLConnector(host="localhost", user="user",password = "password",database="db1")
k = mysql.executeSQL("show databases")
print(k)
k = mysql.executeSQL("show databases")
print(k)

## -- SQLLITE ----
import sqlite3

con = sqlite3.connect("a.b")
k  =con.cursor()
k.execute("select sqlite_version();")
r = k.fetchall()
for row in r:
    print(row)
k.execute("create table tmp (id integer, val string);")
for row in k.fetchall():
    print(row)
    
k.execute("insert into tmp values (1,'deep');")
for row in k.fetchall():
    print(row)
    
k.execute("select * from  tmp ;")
print(k.description)
for row in k.fetchall():
    print(row)
    

###########################
# Custom logging
###########################


import sys, inspect, time

class Logger():
    
    def __init__(self, name = None):
        self.name = name
    
    def info(self,msg):
        caller = inspect.currentframe().f_back.f_code.co_name
        this_time = time.asctime()
        print("{} | {} | {} | {}".format(this_time,self.name,caller,msg))

    def error(self,msg):
        caller = inspect.currentframe().f_back.f_code.co_name
        this_time = time.asctime()
        print("{} | {} | {} | {}".format(this_time,self.name,caller,msg))
        
class Grid:
    def __init__(self,row,col):
        self.logger = Logger(self.__class__.__name__)
        self.row = row
        self.col = col
        self.grid = list()
        for i in range(0,row):
            cols = [None] * col
            self.grid.append(cols)
            for j in range(0,col):
                cell = "({},{})".format(i,j)
                self.grid[i][j] = cell
        self.logger.info("Initiated")
        

    def __repr__(self):
        print(self.grid)
        s = ""
        for row in self.grid:
            s = s+ str(row) + "\n"
        return s
        
    def moveRight(self):
        self.logger.info("moving")
        
class Another:
    def __init__(self):
        logger = Logger(self.__class__.__name__)
        logger.info("Initiated")
        
another = Another()
        
grid = Grid(3,4)
grid.moveRight()



#######################
### Recursion & Dynamic programming
#######################

x,y = 15,18
def gridTravel(m,n,d = dict()):
    # print(m,n,d)
    if (m == 1) or (n==1): 
        return 1
    else:
        key = "{}_{}".format(m,n)
        if key in d:
            return d[key]
        else:
            res = gridTravel(m-1,n,d) + gridTravel(m,n-1,d)
            d[key] = res
            return res

t1 = time.time()
print(gridTravel(x,y))
t2 = time.time()
print(t2-t1)

def gridTravel(m,n,d = dict()):
    if (m == 1) or (n==1): 
        return 1
    else:
        return gridTravel(m-1,n,d) + gridTravel(m,n-1,d)

t1 = time.time()
print(gridTravel(x,y))
t2 = time.time()
print(t2-t1)

def fib(x,d = dict()):
    if x<=2: 
        return 1
    else:
        if x in d:
            return d[x]
        else:
            d[x] = fib(x-1,d) + fib(x-2,d)
            return d[x]
    
x = 50
print(fib(x))


#############################
# Testing
#############################

from math import pi
import unittest

class Student(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_string(cls, name_str):
        first_name, last_name = map(str, name_str.split(' '))
        student = cls(first_name, last_name)
        return student
    
    @staticmethod
    def area(r):
        if (not isinstance(r,int)):
            raise TypeError("illegal Argument {argument}".format(argument = r))
        if (r<0):
            raise ValueError("Incorrect input {radius}".format(radius = r))
        else:
            area = (r**2)
            message = "Area of circle with Radius {radius} is {a}".format(radius = r, a = area)
            print(message)
            return area
        
class TestStudent(unittest.TestCase):
    
    def setup
    

    def test_area(self):
        self.assertAlmostEqual(Student.area(2),4)
        self.assertAlmostEqual(Student.area(0),0)
        
    def test_input(self):
        self.assertRaises(TypeError, Student.area, "a")
        self.assertRaises(TypeError, Student.area, 1.1)

        

# scott = Student.from_string('Scott Robinson')
# print(scott)

# print(Student.area(3))
# # print(Student.area(-1))
# print(Student.area(0))
# print(Student.area(3j))


unittest.main()






########################## DATA STRUCTURES ###############################


class QNode:
    
    def __init__(self,data, front = None, back = None):
        self.data = data
        self.front = front
        self.back = back
        
    def __repr__(self):
        return str(self.__dict__)
    

class Q:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __repr__(self):
        msg = "head - {head}\n"
        msg += "tail - {tail}"
        return msg.format(head = self.head, tail = self.tail)
    
    def is_empty(self):
        if (self.head is None):
            return True
        else:
            return False
    
    def enq(self, data):
        if (self.head is None):
            node = QNode(data)
            self.head = self.tail = node
        else:
            tail = self.tail
            new_node = QNode(data,front = tail)
            self.tail.back = new_node
            self.tail = new_node
        return self
    
    def dq(self):
        if (self.head is None):
            return None
        else:
            node = self.head
            self.head = node.back
            if (node.back):
                node.back.front = None
            return node
    
    def traverse(self, reverse = False):
        print(20 * "-")
        if (not reverse):
            node = self.head 
            while (node is not None):
                print(node)
                node = node.back
        else:
            node = self.tail
            while (node is not None):
                print(node)
                node = node.front
                

    
    
# q = Q()
# # print(q)
# q.enq(10).enq(20).enq(30).enq(40)
# # print(q)

# q.dq()
# q.traverse()
# q.dq()
# q.traverse()
# q.dq()
# q.traverse()
# q.dq()
# q.traverse()
# q.dq()
# q.traverse()
            
        
        


class TNode:
    """
    Node contains the data and the children
    data -> contains the data
    left -> points to left child
    right -> points to right child
    """
    
    
    def __init__(self,data, left = None, right = None):
        """
        Initiate TreeNode 
        """
        self.data = data
        self.left = left
        self.right = right
        
        
    def __repr__(self):
        """
        Return TNode as a String
        """
        data = "[{}]".format(self.data)
        
        if (self.left is not None):
            left = "[{}]".format(self.left.data)
        else:
            left = "[NONE]"
        
        if (self.right is not None):
            right = "[{}]".format(self.right.data)
        else:
            right = "[NONE]"
            
        
        return "{} <- {} -> {}".format(left,data,right)
    
class Tree:
    """
    Implements Tree functionalities
    
    1. Insert
    2. Delete
    3. Search (BFS / DFS)
    
    """
    
    def __init__(self):
        self.root = None

        
    def insert(self, data:int, node = None):
        """
        Makes the node as root, if tree is empty or if node is None.
        Else, inserts the data at right location in the tree traversing from given node.
        """
        
        if (self.root is None):
            # print("Inserted {} at root".format(data))
            newNode = TNode(data)
            self.root = newNode
        else:
            if (node is None):
                node = self.root
                # print("\n\ninserting {}\n\n".format(data))
                self.insert(data,node)
            else:
                if (data <= node.data):
                    # print("""make left operation on {}""".format(node))
                    if (node.left is None):
                        newNode = TNode(data)
                        node.left = newNode
                    else:
                        self.insert(data,node.left)
                else:
                    # print("""make right operation on {}""".format(node))
                    if (node.right is None):
                        newNode = TNode(data)
                        node.right = newNode
                    else:
                        self.insert(data,node.right)  
        return self
    
    
    
    def insert_elements(self, data:list, node = None):
        """inserts a given list of integers into the Tree"""
        
        for element in data:
            self.insert(element)
        
        return self
    
    
    
    def __bfs__(self,data,q:Q):
        """internal function to implement recursive breadth first search"""
        
        print("breadth first search for {} in {}".format(data,q))
        
        if (q.is_empty()):
            return None
        else:
            qNode = q.dq()
            node = qNode.data
            if (data == node.data):
                print("FOUND {} in {}".format(data,node))
                return node
            else:
                if (node.left is not None):
                    q.enq(node.left)
                if (node.right is not None):
                    q.enq(node.right)
                return self.__bfs__(data,q)
    
    
    
    def bfs(self,data):
        """breadth first search"""
        
        print("breadth first search")
        
        if (self.root is None):
            return None
        else:
            node = self.root
            q = Q()
            q.enq(node)
            return self.__bfs__(data,q)



import random
inputs = list(range(-20,20))
random.shuffle(inputs)


tree = Tree()
tree.insert_elements(inputs)
tree.insert(100).insert(200).insert(-100).insert(250)
              
k = tree.bfs(100000)
print(k)



##########--------------- BLOOM FILTER -------------------------################

# https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/


import hashlib
import math

class BloomFilter:
    def __init__(self, size, probability):
        
        self.size = size
        self.probability = probability
        self.bitSize = self.__getArraySize__(size, probability)
        self.bitarray = [0] * self.bitSize
        self.hashCount = self.__getNumberOFHashFunctions__(self.bitSize, size)
        
    def __repr__(self):
        return str(self.__dict__)
        
    def __getArraySize__(self, n, p):
        m = -(n * math.log(p))/(math.log(2)**2)
        return int(m)
    
    def __getNumberOFHashFunctions__(self, m, n):
        k = (m/n) * math.log(2)
        return int(k)
    
    def __getHash__(self, object):
        func = hashlib.md5()
        func.update(object.encode())
        return func.hexdigest()
    
    def __getBitPositions__(self, object):
        bitPositions = []
        for i in range(self.hashCount):
            hexDigest = self.__getHash__(("{}_{}".format(object,i)))
            # print(hexDigest)
            bitPositions.append(int(hexDigest,16) % self.bitSize)
        return bitPositions
    
    def add(self, object):
        bitPositions = self.__getBitPositions__(object)
        # print("bitPositions", bitPositions)
        for position in bitPositions:
            self.bitarray[position]=1
    
    def check(self, object):
        bitPositions = self.__getBitPositions__(object)
        for position in bitPositions:
            if self.bitarray[position] == 0:
                return False
        return True

            
        

    
bloomf = BloomFilter(20, 0.05)

# bloomf.add("cat")
# print(bloomf.check("cat"))
# bloomf.add("cat1")
# print(bloomf.check("cat1"))
# bloomf.add("cat2")
# print(bloomf.check("cat2"))
# # print(bloom)

# words to be added
word_present = ['abound','abounds','abundance','abundant','accessable',
                'bloom','blossom','bolster','bonny','bonus','bonuses',
                'coherent','cohesive','colorful','comely','comfort',
                'gems','generosity','generous','generously','genial']
 
# word not added
word_absent = ['bluff','cheater','hate','war','humanity',
               'racism','hurt','nuke','gloomy','facebook',
               'geeksforgeeks','twitter']
 
for item in word_present:
    bloomf.add(item)
    
test_words = word_present[:10] + word_absent
# shuffle(test_words)
for word in test_words:
    if bloomf.check(word):
        if word in word_absent:
            print("'{}' is a false positive!".format(word))
        else:
            print("'{}' is probably present!".format(word))
    else:
        print("'{}' is definitely not present!".format(word))
        

##### --- SINGLETON ---- #####

class Person(object):
    
    _instance = None
    
    def __new__(cls, name, age):
        if cls._instance is None:
            cls._instance = super(Person,cls).__new__(cls)
            cls._instance.name = name
            cls._instance.age = age
        return cls._instance
    
    def __repr__(self):
        return str(self.__dict__)
            
    
p = Person("deepak",10)
print(p)
# {'name': 'deepak', 'age': 10}
p2 = Person("a",1)
print(p2)
# {'name': 'deepak', 'age': 10}
print(p == p2)
# True            

##################################
######### Non Blocking Q #########
##################################

import threading, collections, time, random, concurrent

class NonBlockingQ:
    
    def __init__(self,capacity):
        
        self.capacity = capacity
        self.currentSize = 0
        self.lock = threading.RLock()
        self.q = collections.deque()
        
    def __repr__(self):
        return str(self.__dict__)
        
    def enq(self,item):
        
        with self.lock:
            if (self.capacity == self.currentSize):
                return False
            else:
                self.q.append(item)
                self.currentSize += 1
                return True
                
    def dq(self):
        
        with self.lock:
            if (self.currentSize == 0):
                return False
            else:
                self.currentSize -= 1
                return self.q.popleft()

def produce(q: NonBlockingQ):
    item = 1
    while True:
        
        print("producing {}".format(item), flush = True)
        result = q.enq(item)
        print("produce result {}".format(result), flush = True)
        if (not result):
            print("sleeping producer ... [{}]".format(
                threading.current_thread().getName()), flush=True)
            time.sleep(random.randint(1, 3))
        else:
            item+=1
            
        if (item == 15):
            print(threading.current_thread().getName(), "COMPLETE", flush = True)
            return
        
        
def consume(q : NonBlockingQ):
    result = 0
    while True:
        
        result = q.dq()
        if (result):
            print("result is [{}] from  ... [{}]".format(result, 
                                                         threading.current_thread().getName()), flush=True)
        else:
            print("sleeping consumer ... [{}]".format(
                threading.current_thread().getName()), flush=True)
            time.sleep(1)
            
        if (result > 12):
            return
            
nbq = NonBlockingQ(100)

            
t1 = threading.Thread(target = produce, name = "Producer", args = (nbq,))
t2 = threading.Thread(target = consume, name = "Consumer", args = (nbq,))

t1.start()
t2.start()

print("End of Main")


############## FUTURES #################
import threading, collections, time, random, concurrent

class NonBlockingQ:
    
    def __init__(self,capacity):
        
        self.capacity = capacity
        self.currentSize = 0
        self.lock = threading.RLock()
        self.q = collections.deque()
        self.put_q = collections.deque()
        self.get_q = collections.deque()
        
    def __repr__(self):
        return str(self.__dict__)
        
    def enq(self,item):
        
        with self.lock:
            future = None
            if (self.capacity == self.currentSize):
                future = concurrent.futures.Future()
                self.put_q.append(future)
            else:
                self.q.append(item)
                self.currentSize += 1
                if (len(self.get_q) >0):
                    next_awaiting_get:concurrent.futures.Future = self.get_q.popleft()
                    next_awaiting_get.set_result(True)
            return future
                
    def dq(self):

        with self.lock:
            result, future = None, None
            if (self.currentSize == 0):
                future = concurrent.futures.Future()
                self.get_q.append(future)
            else:
                self.currentSize -= 1
                if (len(self.put_q) >0):
                    next_awaiting_put:concurrent.futures.Future = self.put_q.popleft()
                    next_awaiting_put.set_result(True)
                return self.q.popleft(), future
            return result, future
                

def produce(q: NonBlockingQ):
    item = 1
    while True:
        
        print("producing {}".format(item), flush = True)
        future:concurrent.futures.Future = q.enq(item)
        print("produce result {}".format(future), flush = True)
        if (future):
            while (future.done() == False):
                print("sleeping producer ... [{}]".format(
                    threading.current_thread().getName()), flush=True)
                time.sleep(random.randint(3, 5))
        else:
            item+=1
            
        if (item == 15):
            print(threading.current_thread().getName(), "COMPLETE", flush = True)
            return
        
        
def consume(q : NonBlockingQ):
    result = 1
    while True:
        
        result, future = q.dq()
        if (not future):
            print("result is [{}] from  ... [{}]".format(result, 
                                                         threading.current_thread().getName()), flush=True)
        else:
            while (future.done() == False):
                print("sleeping consumer ... [{}]".format(
                    threading.current_thread().getName()), flush=True)
                time.sleep(random.randint(1,3))
            
        if (result and result == 14):
            return
            
nbq = NonBlockingQ(100)

t2 = threading.Thread(target = consume, name = "Consumer", args = (nbq,))
t1 = threading.Thread(target = produce, name = "Producer", args = (nbq,))


t1.start()
t2.start()

print("End of Main")

