# Functions:
# A function is a block of code that performs a specific task.
# It allows us to group instructions together and reuse them whenever we needed.
# Instead of writing the same code again and again, we just define a function once and call it whenever required.
# Syntax:
# def function_name(parameters):
#     # function body cade
#     return value # optional
# function_name()
# # example:
# def greet():
#     print("Hello World!")

# # Calling a Function:
# # Calling a Function means telling python to run the code inside a function by using it's name followed by paranthesis().
# # If the function needs the input (paramter), We peovide values (argument) inside the paranthesis.
# # When we call a function, python jumps to the function, excutes it's code, and then comes back to continue the program.
# def greet(name,branch): # function name
#     print("Hello World!",name,branch) #
#     greet("Shiva","CSE-AI&ML") # calling a function.
    
    # passing parameters and arguments
    # parameters: a variable declared inside the function definition.
    #it's act like an empty container waiting to recieve a value.
    # arguments: the actual value we pass 
def greet(name):
    print("hello",name)
greet("pradeep")
 # same task without function .
name="pradeep" # here nameis input variable (parameter),and "pradeep" is value to the paerameter(argument).
print("hello",name)
        
        
    # types of functions arguments:
    # a.positional arguements in the same order as the function parameter,they are called positional arguments.
   # here the order (position) is very important.
def greet(rollno,name): # step2 values store
    print("hello",name,"your rollnois",rollno) #step3: execute the line 
greet("f9","pradeep") # step1:function calling
 
    #b. keyword arguments:
    # when we pass values or arguments by writing the parameter (variable=value),they are called as keyword arguments.
def greet(rollno,name):
    print("hello",name,"your rollmo is",rollno)
greet(name="pradeep",rollno="f9")

# default arguments:
# when a parameter has default value(assigning the value in parameter) i nthe function definition, it becomes a default argument.
def greet(name="student"):
    print("hello",name)
greet()
greet("pradeep")

#d. variable-length arguments:
#sometimes we don't know how many arguments will be passed to a function.
# python provides twp special ways to handle this:
#1. *args: (variable-length arguments):
#collects multiple values into a tuple.
#l=(10,20,30,40,50)
def sum1(*list1):
    sum2=0
    for i in range(len(list1)):
        sum2 = sum2 + list1[i]
    print(sum2)
    print(type(list1))
sum1(10,20,30,40,50)

#2.**kwargs:(keyword variable-length arguments)
# collects multiple key=value pair into a dictionary.
def details(**info):
    for i,j in info.items():
      print(i,":",j)
details(name="pradeep",rollno="f9",branch="csm")

#scope of the variable:
# the scope of a variable means the part of the program where that variable can be accessed or used.
# in python, variables can be local and global, depending on where they created .
# local varioable:
# a variable declared inside a function is called a local variable.
# it exists only while the function is running.
#it cannot be used outside that function .
#  global variable:
# a variable declared outside all function is called a global variable.
#it can be accessed anywhere in the program(inside or outsidefunction).
x=10 # global variable
def var1():
    x=5  #  local variable
    print("inside var1 function",x)
var1() 
def var2():
    print("inside var2 function ",x)
var2()

print("outsidefunction",x)

#lamda function:
#normal function:
def sqe(a):
    print(a*a)
sqe(5)  
# lamda function
squ = lambda a:a*a
print(squ(5))