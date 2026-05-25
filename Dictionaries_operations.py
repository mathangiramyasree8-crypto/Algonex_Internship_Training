Student={       #creating dictionary
    'name':'ramya',
    'role':'Intern'
}
print(Student)
Student={       #creating dictionary
    'name':'ramya',
    'role':'Intern',
    'name':'puri',
    'age':20
}
print(Student)  # replacing the name
print(Student['age'])  #to get particular index
print(Student.get('name')) # for indexing
print(Student.keys()) # All keys in a list ->.keys()
print(Student.items()) # All items in a list->.items()
print(Student.values()) #All values in a list ->.values()
Student['clg']='MJR'  # Add new key-value pair
print(Student)
Student['age']=19  # Modify value
print(Student)
Student.pop('age') #remove element
print(Student)
Student.update({'Role number':12}) #it will add in the dictionary if not present otherwise it will be replaced
print(Student)
skills={'language':'python'}
print(skills.clear()) # clear  entire dictionary
#loop keys
for key in Student:  #loop through dictionary
    print(key)
#loop values
for value in Student.values():
    print(value)
print('name'in Student)   #checking existence
print(len(Student))  #finding length
new_Student=Student.copy()  # copy dictionary
print(new_Student)    #Nested dictionary
P={'A1':{'name':'Ramya'},
   'A2':{'age':20}
   }
print(P)

