'''𝑰𝒇 𝟏𝟎𝟎 𝒔𝒕𝒖𝒅𝒆𝒏𝒕𝒔 𝒋𝒐𝒊𝒏 𝑨𝒍𝒈𝒐𝒏𝒆𝒙, 𝒉𝒐𝒘 𝒅𝒐 𝒘𝒆 𝒔𝒕𝒐𝒓𝒆 𝒂𝒍𝒍 𝒕𝒉𝒆𝒊𝒓 𝒅𝒂𝒕𝒂 𝒑𝒓𝒐𝒑𝒆𝒓𝒍𝒚?
- one variable not enough kadaa
- one list saripothundaa
- need structured collections right soo -> Now dictionaries become meaningful avuthaay'''

# Create a dict with your own details (name, age, DOB, DOJ, role, Batch_type, cgpa, location, amount)
# Let's build mini-project Intern Management System

print('Intern Student Management')
students = []

for i in range(2):
    print(f"\nEnter Student {i+1} Details")

    student = {}

    # Dictionary values
    student["name"] = input("Enter name: ")
    student["role"] = input("Enter target role: ")
    student["cgpa"] = float(input("Enter CGPA: "))

    # List
    projects = []

    p1 = input("Enter Project 1: ")
    p2 = input("Enter Project 2: ")

    projects.append(p1)
    projects.append(p2)

    student["projects"] = projects

    # Set for unique skills
    skills = set(input("Enter skills separated by space: ").split())

    student["skills"] = skills

    # Tuple for fixed student ID
    student["student_id"] = (i+1, "ALG2026")

    students.append(student)

# All students
for student in students:

    print(f"Student ID : {student['student_id']}")
    print(f"Name : {student['name']}")
    print(f"Role : {student['role']}")
    print(f"CGPA : {student['cgpa']}")

    print("Projects :")

    for project in student["projects"]:
        print("-", project)

    print("Skills :", student["skills"])

    # Eligibility Check
    if student["cgpa"] >= 7:
        print("Status : Eligible")
    else:
        print("Status : Need Improvement")

    print("=" * 40)
    # https:https://github.com/mathangiramyasree8-crypto/Aalgonex_Intern_Management_System.git