#area of circle
pi=3.14
r=7
a=(pi*r**2)
print(a)
#area of atriangle
b=45
h=8
t=(1/2*b*h)
print(t)
# resume
#a1=input("enter your name:")
#a2=input("enter your age:")
#a3=input("enter your college:")
#area of triangle
#height=int(input("enter the height value:"))
#base=int(input("enter the base value:"))
#AOT=1/2*height*base
#print(AOT)
#FINDING SQUARE AND CUBE OF A NUMBER
#x=int(input("enter the value:"))
#sq=x**2
#print("square of",x,"is:",sq)
#y=int(input("enter the value:"))
#cube=y**3
#print("cube of",y,"is:",cube)
#distance conversion 
# km-->m,m-->cm
#dis=25 #m
#km=dis/1000
#m=dis*1000
#m1=dis/100
#cm=dis*100
#miles=km*1.6

#find the number whether it is even or odd
#even=0,2,4,6,8,10,......
#odd=1,3,5,7,9,11,.......
# number=int(input("enternumber:"))
# if number%2==0:
#     print("number is even")
# else:
#     print("number is odd")
# #eligibility for voter id

# age=int(input("tell your age:"))
# id=input("do you have voter card: ")
# if  age>18:
#     print("yes, i am above 18")
# if id=="yes":
#     print("go give your vote")
# else:
#     print("your not eligible")
#leap year or not
year= int(input("enter the year:"))
if(year%4==0 and year%100!=0) or year%400==0:
    print("it is a leap year.")
else:
    print("it's not a leap year.")
