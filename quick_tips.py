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

## URL parsing


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
    


