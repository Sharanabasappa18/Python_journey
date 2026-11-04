##1
class car:
    name="Toyota supra"
    color="black"
    brand="Toyota"
c1=car()
print(c1.name)
print(c1.color)
print(c1.brand)

##2
class student:
    
    def __init__(self,name,marks):    #constuctor
        self.name=name
        self.marks=marks
        print("adding new student in the database")
s1=student("sharan",99)            #object
print(s1.name,s1.marks)
s2=student("haulk",88)
print(s2.name,s2.marks)