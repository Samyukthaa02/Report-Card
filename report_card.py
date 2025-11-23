id=int(input("enter student id:"))
name=input("enter student name:")
dict={}
n=int(input("enter number of subjects:"))
for i in range(n):
    sub=input("enter subject name:")
    mark=int(input("enter mark:"))
    dict[sub]=mark
print("-----report card-----")
print("student id:",id)
print("student name:",name)     
print("marks:")
for sub,mark in dict.items():
    print(sub,":",mark)     

avg=sum(dict.values())/n
print("average marks:",avg) 
if avg>=90:
    grade='A'
elif avg>=80:
    grade='B'
elif avg>=70:
    grade='C'   
elif avg>=60:
    grade='D'   
else:
    grade='F'
print("grade:",grade)
