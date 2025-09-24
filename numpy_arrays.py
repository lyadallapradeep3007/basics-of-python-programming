#numpy:
# numpy(numerical python) is a python library used for scientific and mathematical computing.
#  it privides :
#  powerful array objects (more effective than python lists).
#  vectorised operations (fast element-wise calculations.)
#  support for linear algebra,statistics ,random numbers operations etc
#importing the numpy library,
import numpy as np
import array as arr
#creating an array with numpy:
# 1d aray:
a1d=np.array([1,2,3,4,5])
print(a1d)
#2d array:
a2d=np.array([[1,2,3],[4,5,6],[7,8,9]]) 
print(a2d)
# [
#   123
#  456
#   789
# ]
 #methods and operations in numpy arrays:
 # 1. basic array information methods:
a=np.array([1,2,3,4,5])
 # ndim: returns the number of dimensions of the array.
print(a.ndim)
print(a2d.ndim)
#shape: returns a tuple showing the sizes of the array in each dimensions(rows,columns, etc..) 
print(a2d.shape) 
#size: returns the total number of elements in the array.
print(a2d.size)
# dtype: returns the datatype of the elements in the arraay.
print(a2d.dtype) #= type

# 2. crating an array with numpy:
# zeroes: creates an array of 6 zeros
print(np.zeros(6)) #
#ones:creates an array of 12ones
print(np.ones(12))
# arange:creates an array from 1-->10 based on the ranges. 
print(np.arange(1,11,1))  #1 2 3 4 5 6 7 8 9 10
print(np.arange(0,11,2)) # 0 2 4 6 8 10
print(np.arange(1,11,2)) # 1 3 5 7 9 
#linspace:creates 3 numbers evenly spaced between 0 and 1
print(np.linspace(0,1,3)) # ) 0 0.5 1 

# mathematical operations:
a=np.array([1,2,3,4,5])
l=[1,2,3,4,5]
print(a+6)
print(a-1)
print(a*2)
print(a/2)
print(a//2)
print(a**6)

#aggregate functions:
a=np.array([1,2,3,4,5])
# sum():
print(np.sum(a))
# mean:
print(np.mean(a))
# max:
print(np.max(a))
# min:
print(np.min(a))
# median:
print(np.median(a))
#  std:
print(np.std(a))
# cumprod:
print(np.cumprod(a))

#matrix operations:
mat1=np.array([[1,2,3],[4,5,6],[7,8,9]])
mat2=np.array([[9,8,7],[6,5,4],[3,2,1]])
print(mat1+mat2)
print(mat1**2)
print(mat1*mat2)
#dot():
print(np.dot(mat1,mat2))
#transpose:
print(np.transpose(mat1))