import hashlib
print(hashlib.algorithms_guaranteed)
# {'sha3_256', 'sha512', 'sha3_384', 'md5', 'shake_128', 'blake2s', 'sha256', 'sha1', 'shake_256', 'sha3_224', 'sha224', 'blake2b', 'sha384', 'sha3_512'}
h = hashlib.sha3_256("Asas".encode()) # choose the hash function
hash_code = h.hexdigest() # get the hexcode
int_of_hash_code = int(hash_code,16) # convert to integer
int_of_hash_code_8 = int_of_hash_code % (10**9) # get 9 digit equivalent
print(hash_code)
# 98f708dd86ffbeddaa426c034899257a6899ca2ae942e034defc9a7f7c11ac54
print(int_of_hash_code)
# 69188025395992794435712573390023901321732098225068112830243905783543696043092
print(int_of_hash_code_8)
# 696043092 --> guaranteed to be same value
print(hash("hello world"))
# -2933577829885198641 --> this changes everytime | no guarantee
print(abs(hash("hello world"))%(10**9))
# 716272476 --> this changes everytime | no guarantee
print(hash("hello world")%(10**9))
# 826483526 --> this changes everytime | no guarantee


# -------------------- Usecase --------------------

# Lets say - we have a limited list of servers
# We have a large number of keys 
# we would like to hash the values in a way - an addition or removal of server results in minimal re-hashing.
# ------------------------------------------------


# -------------------- INPUT --------------------
# Key list
# ------------------------------------------------

import hashlib

# lets say we are attempting to hash the following keys...
keys = list(hashlib.algorithms_guaranteed)
for key in keys: print(key)
# sha3_256
# sha224
# sha3_512
# shake_256
# md5
# sha3_384
# blake2b
# sha512
# sha256
# shake_128
# sha1
# sha384
# blake2s
# sha3_224  

# Simple attempt at hashing...


# -------------------- STEP 1 --------------------
# Build a logical mapping of location (labels) to servers
# ------------------------------------------------

# This will hold the logical location to physical server mapping
location_list = list()
# say we have 10 servers & we would like to assign 10 logical locations per server
servers = 10
locations_per_server = 10
# Assign Roundrobin labels for each bucket
for i in range(1,locations_per_server*servers+1):
    location_list.append((i,i%servers+1))
print(location_list)
# [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 1), (11, 2), (12, 3), (13, 4), (14, 5), (15, 6), (16, 7), (17, 8), (18, 9), (19, 10), (20, 1), (21, 2), (22, 3), (23, 4), (24, 5), (25, 6), (26, 7), (27, 8), (28, 9), (29, 10), (30, 1), (31, 2), (32, 3), (33, 4), (34, 5), (35, 6), (36, 7), (37, 8), (38, 9), (39, 10), (40, 1), (41, 2), (42, 3), (43, 4), (44, 5), (45, 6), (46, 7), (47, 8), (48, 9), (49, 10), (50, 1), (51, 2), (52, 3), (53, 4), (54, 5), (55, 6), (56, 7), (57, 8), (58, 9), (59, 10), (60, 1), (61, 2), (62, 3), (63, 4), (64, 5), (65, 6), (66, 7), (67, 8), (68, 9), (69, 10), (70, 1), (71, 2), (72, 3), (73, 4), (74, 5), (75, 6), (76, 7), (77, 8), (78, 9), (79, 10), (80, 1), (81, 2), (82, 3), (83, 4), (84, 5), (85, 6), (86, 7), (87, 8), (88, 9), (89, 10), (90, 1), (91, 2), (92, 3), (93, 4), (94, 5), (95, 6), (96, 7), (97, 8), (98, 9), (99, 10), (100, 1)]


# -------------------- STEP 2 --------------------
# Build mapping function to fetch location-server details
# ------------------------------------------------

def find_server(location,location_list):
    server = None
    for label in location_list:
        if (label[0] == location):
            server = label[1]
        else:
            continue
    return server

# -------------------- STEP 3 --------------------
# Implement a simple Hash Function
# ------------------------------------------------

def hash_key(key,location_list):
    # Hash the key using standard hash library function
    hashed = hashlib.sha3_512(key.encode())
    hash_hex = hashed.hexdigest()
    # convert to Integer
    hashed_int = int(hash_hex,base = 16)
    # limit the value to available server count
    location = hashed_int % len(location_list)
    # find the actual physical server
    server = find_server(location,location_list)
    return (key,location,server)

# -------------------- DEMO --------------------
# Find the logical location & physical server for each key
# ------------------------------------------------

for hash_me in keys:
    print(hash_key(hash_me,location_list))

# ('sha1', 81, 2)
# ('sha384', 1, 2)
# ('sha256', 89, 10)
# ('blake2b', 85, 6)
# ('md5', 62, 3)
# ('blake2s', 60, 1)
# ('shake_128', 91, 2)
# ('sha512', 70, 1)
# ('shake_256', 49, 10)
# ('sha224', 92, 3)
# ('sha3_256', 6, 7)
# ('sha3_384', 5, 6)
# ('sha3_512', 95, 6)
# ('sha3_224', 76, 7)
