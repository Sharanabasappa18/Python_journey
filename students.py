# with open("students.csv") as file:
#     for line in file:
#         # row=line.rstrip().split(",")
#         name,house=line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
#         print(f"{name} is in {house}")
        
        
### printing in sorted way ###
students=[]
with open("students.csv") as file:
    for line in file:
        name,house=line.rstrip().split(",")
        students.append(f"{name} is in {house}")
        
for student in sorted(students):
    print(student)