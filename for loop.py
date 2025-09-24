#loop is a program
#for variable in sequence :
#code block
#range(start value and end value,step value)
# for i in range(10) :
#     print("hello!")
# for i in range (0,30,3) :
#     print(i)
# for i in range(1,10,2):
#     print("***welcome***")
#     #print the numbers from 9 to 27
# for i in range(9,28):
#     print(i)
#     #usijng default values the number print upto 15.
# for i in range(16):
#     print(i)
# for i in range(10,-1,-2):
#     print(i)
#     #print the even numbers from 0 to 20
#     for i in range(0,21,2):
#         print(i)
#print the squares of a number upto 6
for i in range(0,7,):
    print("squareof",i,i**2)
#using for loop for list
fruits=["apple","banana","mango"]
for fruit in fruits:
    print(fruit)
fruits="apple"
for i in fruits:
    print(i)
    
#5 table:
for i in range(1,11):
    print("5x",i,"=",5*i)
    
#7 table
for i in range(1,11):
    print("7xi",i,"=",7*i)
    
#1+2+3+4+5+....25=?
sum=0
for i in range(1,26):
        sum =sum+i
        print(sum)
# factorial  of 4 
product=1
for i in range (1,5):
    product=product*i
    
    #breaking at some point
    for i in range(1,25):
        print(i)
        if i==7:
            break

#continue

for i in range(1,26):
    if i ==6:
        continue
    print(i)
    
    for i in range(1,30):
        if i%2==0:
            pass
        else:
            print(i)
     
   