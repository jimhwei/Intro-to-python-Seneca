# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:15:48 2020

@author: jimwe
"""

str1=input("first number:")
str2=input("second number:")
x = 0
y = 0

if str1 != str2:
    for i in str1:
        x += ord(i)
    for j in str2:
        y += ord(j)

if str1 == "" or str2 == "":
    print("you didn't enter anything")
elif x > y:
    print("first number is larger than second number")
elif x < y:
    print("second number is larger than first number")
elif x == y:
    print("these numbers are the same")
else:
    print("something went wrong")