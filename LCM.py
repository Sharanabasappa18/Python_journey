# def find_lcm(x,y):
#     if x>y:
#         greater=x
#     else:
#         greater=y
#     while(True):
#         if((greater%x==0) and (greater%y==0)):
#             lcm=greater
#             break
#         greater+=1
#     return lcm
# num1=int(input("Enter the number :"))
# num2=int(input("Enter the number :"))
# num3=int(input("Enter the number :"))
# print("The L.C.M. is", find_lcm(num1, num2))

def find_lcm_three(x, y, z):
    # Find the largest of the three numbers to start our search
    greater = max(x, y, z)
    
    while(True):
        if((greater % x == 0) and (greater % y == 0) and (greater % z == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

num1=int(input("Enter the number :"))
num2=int(input("Enter the number :"))
num3=int(input("Enter the number :"))

print("The L.C.M. is", find_lcm_three(num1, num2, num3))