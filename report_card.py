
while True:
    try:
        student_id = int(input("Enter student id: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer for student ID.")

name = input("Enter student name: ")
subjects_marks = {}

while True:
    try:
        num_subjects = int(input("Enter number of subjects: "))
        if num_subjects > 0:
            break
        else:
            print("Number of subjects must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of subjects.")

for i in range(num_subjects):
    while True:
        sub = input(f"Enter name for subject {i+1}: ")
        if sub.strip(): # Ensure subject name is not empty
            break
        else:
            print("Subject name cannot be empty. Please enter a valid name.")
    
    while True:
        try:
            mark = int(input(f"Enter mark for {sub}: "))
            if 0 <= mark <= 100: # Assuming marks are between 0 and 100
                subjects_marks[sub] = mark
                break
            else:
                print("Mark must be between 0 and 100. Please re-enter.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the mark.")

print("-----report card-----")
print("Student ID:", student_id)
print("Student Name:", name)     
print("Marks:")
for sub, mark in subjects_marks.items():
    print(f"{sub}: {mark}")     

avg = 0
if num_subjects > 0:
    avg = sum(subjects_marks.values()) / num_subjects

print("Average marks:", avg) 

grade = ''
if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'   
elif avg >= 60:
    grade = 'D'   
else:
    grade = 'F'
print("Grade:", grade)
