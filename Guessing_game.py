# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:51:14 2020

@author: jimwe
"""

import random

x = 0
r = random.randint(1,10)
y = 0

while x != r:
    
    x = int(input("Pick a number from 1 to 10:"))

    if x > r:
        print("Your number is too high")
    elif x < r:
        print("Your number is too low")
    elif x == r:
        print("You've won!")
        y = input("do you want to play the game again? (y/n): ")
        if y == "y":
            x = 0
            r = random.randint(1,10)