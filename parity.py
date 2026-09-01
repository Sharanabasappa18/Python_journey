# x=int(input("X value:"))

# if x%2==0:
#     print("Even")
# else:
#     print("Odd")
    
#using own function 
def main():
    x=int(input("X value:"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
        
def is_even(n):

    # if n % 2 == 0
    #     return True
    # else:
    #     return False 
    
#in one line 
    return True if n%2==0 else False   
    
main()  