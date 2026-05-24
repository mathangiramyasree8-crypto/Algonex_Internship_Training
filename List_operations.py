marks=[100,200,300,400,500]
names=['Ramya','Puri','Soni']
skills=['python','SQL','AI']
print(skills[0]) #positive indexing
print(skills[-2]) #negative indexing
print(marks[0:4:1])#stop=stop-1
print(marks[1:])#starts from 1 index to entire string
print(marks[:1])#execute until last string
print(marks[::2])#jump by 2 numbers
print(marks[1:5:-1])
skills=['python','SQL','AI']
skills[1]='Git'  # modify the element at particular index
print(skills)
skills.append('Power BI') #adding elements
print(skills)
print(marks.extend(names)) # combines list
skills.insert(1,"Fast API")#inserting elements
print(skills)
result=skills+marks+names # concatenating list
print(result)
skills=['python','SQL','AI']
skills.remove('AI') #removing particular element
print(skills)
skills.pop() #removing last element
del skills[0] # deleting element at particular index
print(skills)
skills.clear() #clear entire list
print(skills)
print(len(names)) # length of list elements
print('Ramya'in names) # check existence
print(marks.count(1))#count no.of occurrences
print(names.index('Puri')) #Finding index 
marks=[100,200,400,300,500]
marks.sort()#ascending order default
marks[::-1] # reverse list
new_list=marks.copy() #copy list
print(new_list)
skills=['python','SQL','AI'] # Loop through list
for i in skills:
    print(i)
skills=['python','SQL','AI'] #Loop with index
for i in range(len(skills)):
    print(i,skills[i])
numbers=[1,2,3,4,5] #list comprehension
squares=[X*X for X in numbers] # squares of a number
print(squares)
student=[
    ['Ramya','20'],
         ['puri','19']
         ]  #nested list 
print(student[0][0])#0 index in 0th index
print(student[0][-1])
for S in student:   # loop through nested list
    print(S)
for S in student:  #Nested loop
    for value in student:
        print(value)
names=['Ramya','puri']  #Multiple list operations
roles=['AI','Python']
for n,r in zip(names,roles):
    print(n,r)     # combines list together
marks=[100,200,300,400,500]
print(max(marks))#maximum number in the list
print(min(marks)) #minimum  number in the list
print(sum(numbers)) #adds the total
print(numbers*2) # multiply the list
#skills=['python','SQL','AI']  #split string into list
#skills_list=skills.split() # list object has no attribute split ->DOUBT
#print(skills_list)   # enter new list
skills=['python','SQL','AI']
print(','.join(skills))


  
 