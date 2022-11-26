import numpy as np

"""
Given an array input, find the maximum product of two integers in the array
"""

myArray = np.array([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21])
myArray.sort()
arr_length = len(myArray)
max_product = myArray[arr_length-1] * myArray[arr_length-2]
print(max_product)