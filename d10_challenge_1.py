# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:56:15 2020

@author: Jim
"""

#The above module can be used to compare the big file sizes. 
#For example, if you want to see if your 5 TB file is same as the one that your colleague has, 
#you can check their message digest. Try to solve this problem. 
#You can get some idea by looking at the code in this link but do not use md5 and also do not use the file 
#I/O methods that is suggested in this code 
#(https://stackoverflow.com/questions/36873485/compare-md5-hashes-of-twofiles-in-python)

'''
tutorial
import hashlib
m = hashlib.md5()
m.update(b"Nobody inspects")
m.update(b"the spammish repetition")
m.digest()

hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest()
'''

import hashlib

h1 = hashlib.sha256()
file1 = open('C:/Users/jimwe/Desktop/dogo1.jpg','rb')
buf1 = file1.read()
a = h1.update(buf1)
print(str(h1))

h2 = hashlib.sha256()
file2 = open('C:/Users/jimwe/Desktop/dogo2','rb')
buf2 = file2.read()
b = h2.update(buf2)
print(str(h2))

print(str(a) == str(b))
