# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:15:48 2020

@author: jimwe
"""
arr = [-2,0,2,3,6,7,9]
n1 = len(arr) 

def binarySearch(arr, low, high): 
    if (high < low): 
        return -1
      
    # low + (high - low) / 2 
    mid = int((low + high) / 2) 
    midValue = arr[mid] 
  
    if (mid == arr[mid]): 
        return mid 
  
    # Search left  
    leftindex = min(mid - 1, midValue) 
    left = binarySearch(arr, low, leftindex) 
  
    if (left >= 0): 
        return left 
  
    # Search right 
    rightindex = max(mid + 1, midValue) 
    right = binarySearch(arr, rightindex, high) 
  
    return right 

print("Index matching their value is",  binarySearch(arr, 0, n1 - 1))    