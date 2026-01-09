
def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_mark_input(prompt):
    while True:
        try:
            mark = int(input(prompt))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Mark should be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

id = get_positive_integer_input("enter student id: ")
name = input("enter student name: ")

report_card_data = {}
n = get_positive_integer_input("enter number of subjects: ")

for i in range(n):
    sub = input(f"enter name for subject {i+1}: ")
    mark = get_mark_input(f"enter mark for {sub}: ")
    report_card_data[sub] = mark

print("-----report card-----")
print("student id:", id)
print("student name:", name)
print("marks:")
for sub, mark in report_card_data.items():
    print(sub, ":", mark)

if n > 0:
    avg = sum(report_card_data.values()) / n
else:
    avg = 0.0 # Handle case where there are no subjects
print("average marks:", avg)

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
print("grade:", grade)
