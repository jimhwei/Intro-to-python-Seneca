# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 21:56:48 2020

@author: jimwe
"""

lst = [3,4,1,2,9]
key = []
value = []

dictionary = dict(zip(key,value))
#The zip() function returns an iterator of tuples based on the iterable objects.

for i in range(len(lst)):
    key.append(str(lst[i]))
    value.append(lst[i+1:])

for k, v in dictionary.items():
    if (10 - int(k)) in v:
        a = int(k)
        b = 10 - a

if a is not None:
    print(f"Two numbers that add up to 10 are {a} and {b}")
else:
    print(f"No numbers can add up to 10")
    

#brute force
import itertools

integer_array = [3,4,1,2,9]
target = 10
for numbers in itertools.combinations(integer_array,2):
    if sum(numbers) == target:
        print("Their index positions are",[integer_array.index(number) for number in numbers])