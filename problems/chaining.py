"""
Custom Implementation of chaining methods over collections
"""
class Chain:
    def __init__(self,seq):
        self.seq = seq
    
    def filter(self,func):
        self.seq = filter(func,self.seq)
        return self
    
    def map(self,func):
        self.seq = map(func,self.seq)
        return self
    
def isNotSpace(s):
    return not(str(s).isspace())

def isEmpty(s):
    return len(str(s))==0

def upper(s):
    return str(s).upper()

# Lets take this string & apply chaining
words = "this is the first sentence. this is the second sentence."
f = Chain(words.split(' '))

# Apply chaining
for i in f.filter(isNotSpace)\
            .map(upper)\
            .seq:
    print(i)
    
# THIS
# IS
# THE
# FIRST
# SENTENCE.
# THIS
# IS
# THE
# SECOND
# SENTENCE.
