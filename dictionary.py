#dictionary:
#dictionary is a in-built datatype,which is used to store multiple values in a single variable.
#dictionary stores the data in the form of key-values pairs.
#each is unique and works as an index to access its corresponding value.
#A={s1:"name":"pradeep",}
#keys are immutable(cannot be chsnged),while values can be anythging (mutuble).
#dictionaryare:ordered,mutuble,do not allows the duplicate keys
#syntax:
my_dict={
    "key1":"value1",
    "key2":"value2",
    "key3":"value3",
    "key4":"value4"
}
print(my_dict)
#creating a dictionary:
biodata={
    "name":"pradeep",
    "roll.no":"159",
    "branch":"cse aiml",
    "place":"hyderabad"
}
print(biodata)
#accessing the data 
#using square brackets[]:
print(biodata["name"])
print(biodata["branch"])
print(biodata["place"])
print(biodata["roll.no"])
#using get() method
print(biodata.get("name"))
print(biodata.get("roll.no"))
print(biodata.get("branch"))
print(biodata.get("age"))

#get() method is used to avoid getting an error while running the programme.

#adding and updating in dictionary
biodata["age"]=20
print(biodata)
#update
biodata["place"]="balaji nagar"
print(biodata)

#removing in dictionary:
#pop():
biodata.pop("roll.no")
print(biodata)
#popitem():
biodata.popitem()
print(biodata)
#delete
#del(delete): Deletes the keys from dictionary.
del biodata["branch"]
print(biodata)
#clear(): Removes every item from the dictionary.
biodata.clear()
print(biodata)

# Dictionary methods:
# Methods allow you to access dictionary data easily.
BioData = {
    "Name":"pradeep",
    "Roll.No":"f9",
    "Branch":"CSE AI&ML",
    "Place":"Hyderabad",
    "Role":"web developer"
}
# keys(): It prints only the keys of dictionary
print(BioData.keys())
# values(): It prints only the values of dictionary
print(BioData.values())
# items(): It prints both keys and values
print(BioData.items())

# Updating update(): update the multiple values
BioData.update({"Role":"Web Developer","Place":"Hyderabad"})
print(BioData)
 # Loops to iterate the key (by default the Dictionary's will stores the keys value.):
for i in BioData:
    print(i)
# Loops to iterate the keys using keys() method:
for i in BioData.keys():
    print(i)
# Loops to iterate the values using values () method:
for i in BioData.values():
    print(i)
# Loops to iterate the item using items() method:
for i in BioData.items():
    print(i)

# Nested Tuple:
T = (10,(20,30),(40,50))
#i    0    1       2
print(T[2][1])

# Nested Dictionary:

Students = {
    "S1":{"Name":"Shiva", "RollNo":"E7"},
    "S2":{"Name":"Pradeep", "RollNo":"F9"},
    "S3":{"Name":"Pual", "RollNo":"E8"}
}
print(Students["S1"]["Name"])
print(Students["S2"]["RollNo"])
print(Students["S1"]["RollNo"])
print(Students["S2"]["Name"])
print(Students["S3"]["Name"])