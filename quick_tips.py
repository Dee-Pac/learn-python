print("------Randomize------")

import random
l = list(range(1,10))
random.shuffle(l)
print(l)

print("------Sample------")
## 

sample = random.sample(l,3)
print(sample,l)

print("------Hash function------")
## 

import hashlib

h_func = hashlib.sha512()
h_func.update(b"plain_text_data")
hexval = h_func.hexdigest()
intval = int(hexval,16)
two_digit_hash = intval % 10**2
print("hexval [{}] intval [{}] 2_digit [{}]".format(hexval,intval,two_digit_hash))

print("------Remove Duplicates------")
## 

l1 = list(range(1,3)) + list(range(1,5))
print(l1,list(set(l1)))

print("------if list has same entry------")
## 

from collections import Counter
Counter(l1)
l2 = list([1, 2, 4, 2, 3,1])
print(Counter(l1)==Counter(l2))

print("------Dictionary merge------")
## 

keys = [1,2,3,4]
values = ["a","b","c","d"]

kv_pairs = zip(keys,values)
print(kv_pairs)
d1 = dict(kv_pairs)
print(d1)
d2 = {10:"deepak"}
d1.update(d2)
print(d1)


print("------Dictionary to List------")

print(list(d1.items()))


print("------List operations------")
## List slicing, head, tail, reverse

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

## Exception handling

import sys
try:
    "a" +1
except:
    e = sys.exc_info()
    print(e)
finally:
    pass
    

print(" ---- Map  -----")

for i in map(lambda x: x+1,l):
    print(i)
    
print(" ---- reduce  -----")
import functools
print(functools.reduce(lambda a,b:a+b, l))

print(" ---- itertools  -----")

import itertools

print(" ---- permutations  -----")
for i in itertools.permutations(range(0,3),2):
    print(i)
print(" ---- combinations  -----")
for i in itertools.combinations(range(0,3),2):
    print(i)
print(" ---- product  -----")
for i in itertools.product(range(0,3),repeat=3):
    print(i)
    
print(" ---- accumulate  -----")    
import operator
l = range(1,5)
for i in itertools.accumulate(l,operator.mul):
    print(i)
    
## Regex

## Read / write to file

## URL parsing

## Time & Date

## Class, Inheritence

## JSON, CSV

## Multithreading, Multiprocessing



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
    

import sys
try:
    import mysql.connector
    con = mysql.connector.connect(host = "",port = "", user = "", password = "", database = "")
    cur = con.cursor()
except:
    e = sys.exc_info()
    print(e)
finally:
    print(con.close())
