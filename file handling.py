#syntax
# file=open ("file name","mode") # r,w,a,rb,wb,r+,w+
file=open("student.txt","r")
print("file created")
file.close()
#types of read():
# 1. read()==>
file=open("student.txt","r")
content=file.read()
print(content)
file.close()
# 2. readline()==> 
file=open("student.txt","r")
content=file.readline()
content1=file.readline()
content2=file.readline()
# 3. readlines
file=open("student.txt","r")
content=file.readlines()
print(content)
file.close()
# write, writelines
file=open("student2.txt","w")
file.write("hello c++\n")
file.write("hello python\n")
lines=["hellonadhan\n","hello pradeep\n","hello shiva\n"]
file.writelines(lines)
file.close()
file=open("student2.txt","a")
file.write("hello world\n")
file.close()


