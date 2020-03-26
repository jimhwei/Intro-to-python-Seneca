# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:56:15 2020

@author: Jim
"""

#Please read this link (https://leons.im/posts/a-python-implementation-ofsimhash-algorithm/) 
#and install simhash and test it with two files that are similar together 
#and prove that you can find similar contents. 

import re
import simhash
from simhas import simhash

def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

print ('%x') % simhash(get_features('How are you? I am fine. Thanks.')).value
print ('%x') % simhash(get_features('How are u? I am fine.     Thanks.')).value
print ('%x') % simhash(get_features('How r you?I    am fine. Thanks.')).value

from simhash import simhash
print (simhash('aa').distance(simhash('bb')))
print (simhash('aa').distance(simhash('aa')))