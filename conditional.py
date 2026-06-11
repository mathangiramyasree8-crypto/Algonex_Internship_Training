# If conditions are used to execute a block of code only if a certain condition is true. 
current_password = 970114
password=str(input('Enter your password:'))
if password==current_password:
    print('Login success')
else:
    print('Wrong password')



#Student marks grading using elif

marks=float(input('Enter your total marks:'))
if marks>=90 and marks<100:
    print('A+')
elif marks>=80 and marks<90:
      print('A')
elif marks>=75 and marks<80:
     print('B')
elif marks>50 and marks<75:
     print('C')
elif marks>=35 and marks<50:
     print('D')
else:
     print('F')
   

   #nested if statement
cgpa=float(input('Enter your CGPA:'))
skills=input('Enter your skills:')
if cgpa>=7.7:
     if skills=='python':
        print('You are eligible for the internship')
else:
        print('You are not eligible for the internship')


        