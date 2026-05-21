participants = []

count = int(input("How many participants? "))

for i in range(count):
    name = input("Enter name: ").strip().title()
    role = input("Enter role: ").strip().capitalize()
    participants.append({"name": name, "role": role})
    print(f"✓ Hello {name}, your role is {role}!")

print("\n--- Participants ---")
for i, p in enumerate(participants, 1):
    print(f"{i}. {p['name']} - {p['role']}")