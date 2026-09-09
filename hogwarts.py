# students=["hermione","Ron","harry"]
# print(students[0])
# print(students[1])
# print(students[2])

# for students in students:
#     print(students)
    
# using len
# for i in range(len(students)):
#     # print(students[i]) 
#     print(i+1,students[i]) 
    

#dict
# students={
    # "Hermione":"Gryffindor",
    # "Harry":"Gryffindor",
    # "Ron":"Gryffindor",
    # "Draco":"Slytherin",
# }
# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])
# for i in students:
    # print(i,students[i],sep=",")



students=[
    {"name":"Hermione","house":"Gryffindor","patronus":"otter"},
    {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
    {"name":"Ron","house":"Gryffindor","patronus":"Jack Russel terrier"},
    {"name":"Draco","house":"Slytherin","patronus":"None"},
    ]
for student in students:
    print(student["name"],student["house"],student["patronus"],sep=",")









