# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 07:53:11 2020

@author: Jim
"""

'''
there is a sorting algorithm called Quick Sort that used a recursive method. 
Learn how that works.
'''

'''
quick sort is a divide and conquer algorithm using recursion
the idea is to break down a problem continuously until it is
simple enough to be solved
'''

def partition(arr,low,high): 
	i = ( low-1 )		 
	pivot = arr[high]	 

	for j in range(low , high): 

		if arr[j] <= pivot: 
		
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

def quickSort(arr,low,high): 
	if low < high: 

		pi = partition(arr,low,high) 

		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 

arr = [20, 4, 7, 3, 9, 6] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Array based on QuickSort:") 
for i in range(n): 
	print ("%d" %arr[i]), 
