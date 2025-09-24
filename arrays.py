#arrays in python:
# an array is collection of elements ofthe same datatype stored ina continous memory location.
#arrays are used to store multiple values in a single variable.
#why arrays?
#easy to manage multiple values.
#allows faster operations like searching and sorting.
#useful in mathematical and scientific problems
#saves memory
# arrays  vs lists 
 # Importing the array module.
import array as arr

# Creating an array:
Numbers = arr.array('i',[1,2,3,4,5])
print(type(Numbers))
print(Numbers)
# i = integer
# f = float
# u = string 

# Accessing Array Elements.
print(Numbers[0]) # 1
print(Numbers[3]) # 4
print(Numbers[-1]) # 5

# Adding An element in array:
# append():
Numbers.append(7)
print(Numbers)
# insert():
Numbers.insert(2,6)
print(Numbers)
# extend:
Numbers[0]






# pop():

# Updating an Element:
Numbers[0] = 10
print(Numbers) # [10,2,6,3,4,5,7,8,9]

# Looping through Arrays:
for i in Numbers:
    print(i)