#collection data types
# list1=[10,20,30,40,50] #integer values
# fruits = ["banana","mango","cherry"]
# list2=[10.2,20.5,22.45,15.0]
# list3=[True,False,True,False]
# list4=[10,"banana",True,2.6,"True"]
# print(list1[3])
# print(list3[0])
# print(list4[4])
# # by negatve values
# print(list4[-1])
# print(list4[-3])
# print(list4[-4])
# by using slicing
#is used for taking out the part of an item or value from the main list.
# slcl=("prabhas","balayya","pspk","bob","bhaai")
# print(slcl[ :3])
# print(slcl[1:4])
# print(slcl[-3:])

#we can add new items or values to a list in difeerent types
 #1.append
#2.insert
#3.extending

#1.append:adds a single value at the of the list
# kalkicast=["prabhas","kamal","amitab","deepika","ssr"]
# kalkicast.append("disha patani")
# print(kalkicast)

# #2.insert : adds a single value at the particular position using index
# kalkicast.insert(2,"vijay")
# print(kalkicast)

# #3. extending : adds multiple values at once by combining the lists
# kalkicast.extend(["anudeep","mrunal","bujji"])
# print(kalkicast)

# #output =["prabhas","kamal","vijay","amitab","deepika","ssr","disha patani","anudeep","mrunal","bujji"]
# kalkicast.insert(5,"bhrammanandham")
# print(kalkicast)

# #removing elements in list

# #1.remove():removes or deletes the first occurence of the specific items
# kalkicast.remove("mrunal")
# print(kalkicast)
# #2.pop(): deletes the items at the particular position 
# kalkicast.pop(6)
# #3.clear():deletes all the items
# # kalkicast.clear()
# print(kalkicast)
# kalkicast[1]="sandeep"
# print(kalkicast)
# #changing the elements:
# # changing the elements:lists are mutuble,we can change the values after the lists using index
# # kalkicast[1]="sandeep"
# # print(kalkicast)
# # mathematical operators
# #1. concatenation: joins two lists together in one list multiple times
# a=(1,2)
# b=(3,4)
# c=(a+b)
# print(c)
# #2.repetations:repeats  the elements of a list multiple times
# a=[1,2]
# n=int(input("enter a value"))
# b=a*n
# print(b)
# #searching and checking:
# #we can check if an elements or values exists in a list or not:
# #in operator:
# #it is a membership operator,which returns the true values if the elements exists in the lists.
# a=[2,4,6,8,10,12,14]
# if  2 in a:
#     print("yes item is present in the list")
#     #not in operator:
#     #it is a membership operator ,which returns the true values if the elements is not exists in the list,
#     print(3 not in a)
#     #index(): which gives the position of the first occurenceof an element or value .
#     print(a.index(8))
#     #count(): which gives the number of elements in the lists.
#     print(a.count(8))
#     for i in range (10):
#         cnt=0
#         if i == 8:
#            cnt = cnt + 1
#     print(cnt)
#     #sorting:sort()
#     #it arranges elements either in ascending order (small to large) or descending order (large to small).
#     #it flips the list so the last element will become the first element. 
#     st = [25,12,5,31,13,18,7,45,8,55,68]
#     #ao= 5,7,8,12,13,18,25,31,45,55,68
#     st.sort()
#     print(st)
#     #do=68,55,45,31,25,18,13,12,8,7,5
#     st.reverse()
#     print(st) #do=68,55,45,31,25,18,13,12,8,7,5
#     st1=[25,8,4,7,10] #25,10,8,7,4
#     st1.sort(reverse=True)
     
#     #  1 5 4 2 3
#     #  #R=32451 # ao=12345
#     #  #Ao=1 2 3 4 5
     
#     #  #copyingthe list:
#     #  #copying creates a new list with the same elements, so changes in the new list do not affect the original list.
#     frd1=["A","C","D","A","D","B","B",'C',"C","A","A"]
#     frd2=frd1.copy()
#     frd2[2] ="B"
#     print(frd2)
#     #built-in functions with loops:
#     # python programming 
#     st=[25,12,5,31,13,18,7,45,8,55,68]
#     #len():returns the number of elements .
#     print(len(st))  #11
#     #max(): returns the maximum element from the list .
#     print(max(st)) # 68
#     #min(): returns the minimum element from the list.
#     print(min (st))  #5
#     #sum(): returns the total sum of all numeric elements.
#     print(sum(st))  #287 
#     #split concept
#     a= "hello world to the python programming"
#     b=a.split()
#     print(b)
#     #multiple values using input data to the list
#     a=input("enter the values:").split() #10 20 30 40 50
#     print(a)
#     list1=[10,20,30,40,50]
#     #map(v,v)
#     a=list(map(int,input("enter the multiple values:").split()))
#     #a.sort()
#     print(a)
    
#     b=input("enter the multiple values:").split()
#     print()
    
#     #traversing a list:
#     #accessing the elements using a loop
#     #using for loop 
#     cars=["alto","maruti800","ambassador","nano"]
#     print(len(cars))
#     #index   0      1           2           3 
#     for car in range(0,4):
#         print("cars=",car)
        
#     #using index with for loop :
#     a=len(cars)  #4

# for i in range (0,a):
#     print("cars",i,cars[i])

#adding elements using for loop:
#list1="thar","jaguar"."audi","bmw"
# list1=[]
# n=int(input("enter the number of list values :"))
# for i in range(0,n):
#     a=input("enter the list values:")
#     list1.append(a)
# print(list1)

#give the input values to the lists from 0 to 10
# list1=[]
# n=int(input("enter the number of list values :"))
# for i in range(0,n):
#     list1.append(i)
# print(list1)

#sumlist items =10 20 30 40 50 without using sum():
num = [10,20,30,40,50]
sum = 0
for i in num:
    sum= sum + i
print(sum)

#convert["p","y","t","h","o","n"] to pyhton
list=["y","t","h","o","n"]
word="p"
for i in list:
    word=word+i
print(word)   

#find the maximum and minimum number from list without using max() and min()
number=[10,12,33,24,5,76,227,8,98,50]
number.sort()
print(number)
print("maximum number is:",number[-1])
print("minimumnumber is :",number[0])

#find the maximum and minimum number from list without using max() and min()
 
list=[12,23,45,74,568,454,34,1,56,7,4,8,42,55,75]
max1=list[0]
min1=list[0]
for num in list:
    if num >max1:
        max1=num
    if num<min1:
        min1=num
print(max1)
print(min1)