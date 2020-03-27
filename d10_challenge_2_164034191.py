# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:56:15 2020

@author: Jim


#Please read this link (https://leons.im/posts/a-python-implementation-ofsimhash-algorithm/) 
#and install simhash and test it with two files that are similar together 
#and prove that you can find similar contents.
"""
from simhash import Simhash

#file path example: 
'C:/Users/txt1.txt'

def sim(file1,file2):

    file1 = (file1.read()).decode('utf-8')
    a = (Simhash(file1).value)
    
    file2 = (file2.read()).decode('utf-8')
    b = (Simhash(file2).value)
    
    c = b/a
    
    if c == 1.0:
        print("They are the Same")
    
    elif 0.95 <= c <= 1.05:
        print("Quite Similar")
        
    if 0.5 <= c <= 1.5:
        print("Similar")
    
    else:
        print("Not Similar")

file1 = open(input('Input file path 1 here:'),'rb')
file2 = open(input('Input file path 2 here:'),'rb')
#file1 = open('C:/Users/jimwe/Google Drive/Seneca Intro to Python/Midterm 2/txt1.txt','rb')
#file2 = open('C:/Users/jimwe/Google Drive/Seneca Intro to Python/Midterm 2/txt2.txt','rb')

sim(file1,file2)

s = "The distance between the two files:"
i = (Simhash(file1).distance(Simhash(file2)))

print(s,i)