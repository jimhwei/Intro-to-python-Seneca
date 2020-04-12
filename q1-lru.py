# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:57:00 2020

@author: jimwe
"""
'''
#least recently used cache

#data structure 1 cache implementation:
a,b,c,d,e = 1,2,3,4,5
    
#data structure 2 eviction function:
'''


import time

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val 
        self.next = None
        self.next = None
        #helps to insert and remove a node

class LRUCache:
    
    cache_limit = 3
    #our cache is 5
    
    def __init__(self, func):
        self.func = func
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        #easy to know when it's top or bottom
        self.tail.prev = self.head
        
    def __call__(self, *args, **kwargs):
        
        if args in self.cache:
            self.llist(args)
            return f'Cached...{self.cache[args]}'
        
        if len(self.cache) == self.cache_limit:
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]
            
        results = self.func(*args, **kwargs)
        self.cache[args] = result
        node = Node(args, result)
        self._add(node)
        return result
    
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n 
        n.prev = p
    
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = self.tail
    
    def llist(self,args):
        current = self.head
        while True:
            if current.key == args:
                node = current
                self._remove(node)
                self._remove(node)
                break
            else:
                current = current.next

#LRUCache
def ex_func_01(n):
    print(f'Computing..{n}x{n}')
    time.sleep(1)
    return n*n

def ex_func_02(n):
    print(f'Computing...{n}+{n}')
    time.sleep(1)
    return n+n

print(f'\nFunction: ex_func_01')
print(ex_func_01(4)) # Cache: {(4,): 16} <-- 4 is at top / only on here.
print(ex_func_01(5)) # Cache: {(4,): 16, (5,): 25} <-- 4 is at bottom with 5 at top
print(ex_func_01(4)) # Cache: {(5,): 25, (4,): 16} <-- 4 gets called from cache and gets moved to top again.
print(ex_func_01(6)) # Cache: {(5,): 25, (4,): 16, (6,): 36}
print(ex_func_01(7)) # Cache: {(5,): 25, (4,): 16, (6,): 36, (7,): 49} <-- cache limit reached.
print(ex_func_01(8)) # Cache: {(4,): 16, (6,): 36, (7,): 49, (8,): 64} <-- 5 is removed and 8 joins top

print(f'\nFunction: ex_func_02')
print(ex_func_02(8)) # Cache: {(8,): 64}
print(ex_func_02(7)) # Cache: {(8,): 64, (7,): 49}
print(ex_func_02(6)) # Cache: {(8,): 64, (7,): 49, (6,): 36}
print(ex_func_02(4)) # Cache: {(8,): 64, (7,): 49, (6,): 36, (4,): 16} <-- 4 on end + at cache limit. 1 over cache limit 3 = 4
print(ex_func_02(5)) # Cache: {(7,): 49, (6,): 36, (4,): 16, (5,): 25} <-- 8 gets removed and 5 joins the top
print(ex_func_02(4)) # Cache: {(7,): 49, (6,): 36, (5,): 25, (4,): 16} <-- 4 get called from cache and gets moved to top
