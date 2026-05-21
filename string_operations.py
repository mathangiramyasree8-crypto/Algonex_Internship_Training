name='Ramya sree'
print(name[0]) #indexing
print(name.index('a')) # finding index of character
print(len(name)) # length of a string
print(name+'Sree') # append-> add one or more elements
print(name+'Sree',sep='%') #error->one variable and one string function 
#name.append('mathangi') #attribute error
#name.extend('Student') #no extend operator in string
print(name.upper()) #uppercase letters
print(name.lower()) #lowercase letters
print(name.title()) #title
print(name.capitalize()) #capitalize the first letter
print(name.strip()) #remove white spaces before and after 
print(name.lstrip()) #remove left side whitespaces
print(name.rstrip()) #remove whitespaces on right side
print(name.split(','))#split the string
print(name.replace('Ramya','Sree'))#replace the string
print(name.find('sree'))#To find string Index return first character Index of the string
print(name.count('Sree'))#count no.of occurrences
print(name.startswith('Sree'))
print(name.endswith('Sree'))
skills=('python is backend language')
Age='20'
print(skills.join(Age)) # to join the elements with special characters