name=('Ramya','Siri','Puri')
print(name[0]) # accessing tuple elements by using indexing
print(name[-1])
print(name[0:2:1])  #slicing tuple
print(name[1:])
print(name[::1])
print(name[0:2:2])
#name[0]='Anu' # IMMUTABILITY ->CAN'T CHANGE ONCE DECLARED
#print(name)
skills=('python','SQL','AI')
for S in skills:  # looping through skills
    print(S)
print(len(skills)) # tuple length
print('python'in skills) #checking existence
print(skills.count(1)) #no.of occurrences
print(skills.index('SQL')) #find index
#print(name=('puri')) #error ->single  element tuple 
name=('puri',)
print(name)
student='Ramya',20,'AI' #tuple packaging
print(student)
name,role,age=student  # tuple unpackaging
print(name)
print(role)
def get_student():   #Function return example
    return('Ramya',20)
data=get_student()
print(data)
name,age=get_student() #Directly   very clean coding style
print(name)
print(age)
students=(('Ramya',20), #nested tuple
          ('puri',19))
print(students)
print(student[0][0]) #access nested tuples
skills=['python','SQL'] # convert list to tuple
skills_tuple=tuple(skills)
print(skills_tuple)
skills=('python','SQL')  # convert tuple to list
skills_list=list(skills)
print(skills_list)
t1=(1,2,5,4,6)   #tuple concatenation
t2=(1,2,3,4,5)
print(t1+t2)
t3=t1*2 #tuple repetition
print(t3)
