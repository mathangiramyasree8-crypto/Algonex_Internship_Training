student_skills = set(input("Enter your skills : ").split())
job_skills = {"Python", "SQL", "Git"}

matched = student_skills & job_skills
missing = job_skills - student_skills

print(f"Matched : {matched}")
print(f"Missing : {missing}")