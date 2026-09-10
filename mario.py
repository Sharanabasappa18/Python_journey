# def main():
#     print_column(3)
# def print_column(height):
#     # for _ in range(height):
#         # print('#')
#     print("#\n" * height ,end="")
# main()


# def main():
#     print_row(3)
# def print_row(width):
#     print("?" * width)
# main()

def main():
    print_square(3)
def print_square(size):
    
    #For each row in square      &  in place of size we can write number for only one loop 
    for i in range(size):
        
        # #For each brick in row 
        # for j in range(size):
            
        #     # Print brick 
        #     print("#",end="")
        # print()
        # print("#"* size)        #in one line u can print the square without inner j loop 
        print_row(size)
def print_row(width):
    print("#"* width )
main()

            