# error handling:
#   errors are mistakes in a program that stop it from working correctly.
#   excepton is a special type of error that occurs while the program is running.
#   python provides ways to handle eceptions so that the program doesn't crash suddenly.
#  types of error:
# 1. compile-time error:(syntax error)
#  errors that happen when the code is not written correctly (wrong syntax)
# 2. logical error:
# errors when the program runs but gives wrong output because the logic is wrong.
# 3. runtime error:(exceptions)
# errors hsppens when the program is running.
# types of exception in the python :
# 1. zerodivisionerror
# 2. value error 
# 3. index error
# 4. key error
# 5. type error
# 6. filenoterror
 # 7. name eroor
  
# 1. zerodivision error:
try:   
    a=int(input("enter the value: "))
    b=int(input("enter the value"))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("error:division by zero is not possible")
    
# example 2 
try:   
    a=int(input("enter the value: "))
    b=int(input("enter the value"))
    c=a//b
    print(c)
except ZeroDivisionError:
    print("error:division by zero is not possible")
# example 3
try:
    i=3
    n=int(input("enter the value: "))
    if i % n==0:
        print("yes, number is multiple of",n)
    else:
        print("no,number not is multiple of",n)
except ZeroDivisionError:
    print("error: division by zero is not possible")
    
 #  value error:
 try:
    rollno=int(input("enter your rollno: "))
 except ValueError:
    print("error: given value is not in the interger datatype.") 
    
# index error:
try:
    list=(10,20,30)