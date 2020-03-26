# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:56:15 2020

@author: Jim
"""
'''
familiarize yourself with the “re” module 
(https://docs.python.org/3/library/re.html). 
It is an abbreviation for the Regular Expression. 
They are used to find a string with a specific pattern. For example, the phone numbers in Toronto have 10 digits 
and they have this format xxx-yyy-wwww 
Use the re module to check if the user has entered a valid phone number that follows the abovementioned pattern.
'''

import re

print("Regular phone numbers follow xxx-yyy-wwww pattern")
phonenumber= input("Check to see if your phone number is in valid form:")

regex= "\w{3}-\w{3}-\w{4}"

if re.search(regex, phonenumber):
    print("Valid phone number")
else:
    print("Invalid phone number")