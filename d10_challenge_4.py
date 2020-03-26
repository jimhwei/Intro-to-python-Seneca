# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:56:15 2020

@author: Jim
"""

'''
Write a program to count a number of files for each extension in the given directory. 
The program should take a directory name as argument and print count and extension for each available file extension. 
For example, the output would be something like this: python counter.py \yourpathhere 
14 py 
4 txt 
1 csv
'''

import os 
import glob
import collections

path = input(r"Insert your path here:")

os.chdir(path)
cnt = collections.Counter()
for filename in glob.glob("*"):
    name, ext = os.path.splitext(filename)
    cnt[ext] += 1
print(cnt)

'''
#listing all of the items
os.chdir(r"C:/Users/jimwe/Google Drive/Seneca Intro to Python/Midterm 2")
x = glob.glob("*.*")
for i in x:
    print(i)
'''