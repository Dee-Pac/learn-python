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
