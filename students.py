# with open("students.csv") as file:
#     for line in file:
#         # row=line.rstrip().split(",")
#         name,house=line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
#         print(f"{name} is in {house}")
        
        
### printing in sorted way ###
# students=[]
# with open("students.csv") as file:
#     for line in file:
#         name,house=line.rstrip().split(",")
#         students.append(f"{name} is in {house}")
        
# for student in sorted(students):
#     print(student)
    

#### By defining a function ####
# students=[]
# with open("students.csv") as file:
#     for line in file:
#         name,house=line.rstrip().split(",")
#         student={"name":name,"house":house}
#         students.append(student)
        
# # def get_name(student):         
#     # return student["name"]

# # for student in sorted(students,key=get_name,reverse=True):    # use only when defining a function 
# for student in sorted(students,key=lambda student:student["name"]):     # use lambda instead of function 
#     print(f"{student['name']} is in {student['house']}")



## using csv.reader function ##
# import csv
# students=[]
# with open("students.csv") as file:
#     # reader=csv.reader(file)
#     # for name,home in reader:
#         # students.append({"name":name,"home":home})
#     reader=csv.DictReader(file)
#     for row in reader:
#         students.append({"name":row["name"],"home":row["home"]})

 
# for student in sorted(students,key=lambda student:student["name"]):
#     print(f"{student['name']} is from {student['home']}")
        

############ for writing the csv file #############
import csv

name = input("What's your name? ")
home = input("Where is your home? ")

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])












