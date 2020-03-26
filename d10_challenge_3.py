# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:56:15 2020

@author: Jim
"""

#use the information you have gained so far to create a program that 
#asks the user for a topic and search the 
#https://icanhazdadjoke.com and if it finds more than one jokes, 
#then it randomly chooses one of those and shows it to the user.

import requests
from random import choice

url = "https://icanhazdadjoke.com/search"

keyword = input("Let me tell you a joke! Give me a topic:")

response = requests.get(
    url,
    headers={"ACCEPT":"application/json"},
    params={"term":keyword,"limit":10}
)

#print(response.text)

data = response.json()['results']

#print (data)
#print(len(data['joke']))
#print(data["results"])
#print(len(data))

if len(data) > 1:
    num = len(data)
    selection = choice(data)
    line = selection['joke']
    print(f"\nI've got {num} jokes about {keyword}. Here's one: \n {line}")

elif len(data) == 1:
    line = data[0]['joke']
    print(f"\nI've got one joke about {keyword}. Here it is: \n {line}")

else:
    print(f"\nSorry, I don't have any jokes about {keyword}! Please try again.")