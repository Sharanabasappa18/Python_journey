# name=input("enter your name:")
# age=int(input("enter your age:"))
# print(f'{name} is {age} years old')

# a= 'Raj\"hi how are you?\"' 
# b= 'ren''\?'
# print( a+b )

#Type conversion
# a=3;b=3.4
# print(a+b) 

#Type casting
# a=float(4)
# b=7.8
# print(a-b)

# STRINGS: sequence of characters{ IMMUTABLE:cannot change }
# s="string"
# d="concatination"
# print(s+' '+d) #for spacing use ("") or ('') or else give space after the sentence
# print(len(s+d))

 
# #2
# str1="john"
# str="Snow"
# print("The person ", str+str1 ,"\nIs so dangerous person in the GOT",str1+str)

#indexing
# sd="jdkjfkjjhdhahhf djhs djhdhsh"
# print(sd[-5])

#Slicing
# sl="Gameofthrones"
# print(len(sl[2:13:2])) #start=2 , stop=13 , step=2
# print(len(sl))
# print(sl[0:13:-2]) #it gives the empty string because of the (-)negative indexing in wrong place
# print(sl[13:8:-4])

# str="Apnacollege"
# print(str[4:-3])

#String functions
# AC="this is john snow ,The illegimate son of Eddard stark .\nAnd thus the John snow is the half-brother of Robb,Sansa,Arya,Bran,and Rickon stark"
# print(AC)
# print(AC.endswith("W"))
# print(AC.capitalize()) # it capitalizes the first letter only 
# print(AC.replace("john snow","RIO")) #it cannnot replaced the "John snow" because of 1st letter is caps
# print(AC.find("snow"))
# print(AC.rfind("snow"))
# print(len(AC))
# print(AC.count("J"))    #Counts the occurence of substring
# print(AC.count("s"))


#Conditional Statement

# if-else-if
# age=int(input("Enter your age:"))
# if(age>= 700):
#     print(f'Your age is {age} you are Bhoot')
# else:
#     print(f'Your age is {age} you are Insan')


# #Traffic light
# light=input('Enter the light 🚦:')
# if(light=='green'):
#     print(f'The light is 🚦 {light} you can leave ')
# elif(light=='yellow'):
#     print(f'You cant go the light is {light} if you go, the accident may occur ')
# elif(light=='red'):
#     print(f'The light is {light} you cant go ')
# else:
#     print("Your fucked up 😵‍💫 ")


# #NESTING
# age=int(input("Enter the age:"))
# if(age>=79):
#     if(age<=90):
#         print("young")
#     else:
#         print("old")
# else:
#         print("young")


#EVEN or ODD
# num=int(input("Enter the number:"))      
# if(num%2==0):
#     print("Even")
# else:
#     print("Odd")

      #OR#
# num=int(input("Enter the number:"))
# rem=num%2
# if(rem==0):
#     print("Even")
# else:
#     print("Odd")


#GREATEST OF 3 NUMBER
# a=int(input("Enter the 1st number:"))
# b=int(input("Enter the 2nd number:"))
# c=int(input("Enter the 3rd number:"))
# if(a>=b and b>=c):
#     # print("First number is largest",a) 
#     print(f'1st number {a} is largest')
# elif(b>=c):
#     # print("Second number is largest",b)
#     print(f'2nd number {b} is largest')
# else:
#     # print("Third number is largest",c)
#     print(f'3rd number {c} is largest')


#MULTIPLE OF 7 OR NOT
#X=int(input("Enter number:"))
#if(X%12==0):
 #   print("multiple")
#else:
 #   print("not multiple") 
    
from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    free_fields = make_list_of_free_fields(board)
    
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalide move! Please choose a number between 1 and 9.")
                continue
                
            # Map the 1-9 input to (row, col) coordinates
            row = (move - 1) // 3
            col = (move - 1) % 3
            
            if (row, col) in free_fields:
                board[row][col] = 'O'
                break
            else:
                print("That square is already taken! Try again.")
        except ValueError:
            print("Please enter a valid number.")

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row_idx in range(3):
        for col_idx in range(3):
            # If the square contains a number (string or int), it's free
            if board[row_idx][col_idx] not in ['X', 'O']:
                free_fields.append((row_idx, col_idx))
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game.
    
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign: # Horizontal
            return True
        if board[0][i] == board[1][i] == board[2][i] == sign: # Vertical
            return True
            
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
        
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    
    # Simple AI: Pick a random available square
    while True:
        row = randrange(3)
        col = randrange(3)
        if (row, col) in free_fields:
            board[row][col] = 'X'
            break

# --- Main Game Loop to run it all ---
if __name__ == "__main__":
    # Initialize the board. As per instructions, the computer ('X') 
    # usually takes the middle square (5) right at the start.
    board = [
        [1, 2, 3],
        [4, 'X', 6],
        [7, 8, 9]
    ]
    
    print("Welcome to Tic-Tac-Toe!")
    print("Computer plays 'X' and you play 'O'. Computer starts at the center.")
    
    while True:
        display_board(board)
        
        # 1. User's turn
        enter_move(board)
        if victory_for(board, 'O'):
            display_board(board)
            print("Congratulations! You won!")
            break
            
        if len(make_list_of_free_fields(board)) == 0:
            display_board(board)
            print("It's a draw!")
            break
            
        # 2. Computer's turn
        print("Computer is making a move...")
        draw_move(board)
        if victory_for(board, 'X'):
            display_board(board)
            print("Game over! The computer won.")
            break
            
        if len(make_list_of_free_fields(board)) == 0:
            display_board(board)
            print("It's a draw!")
            break  
        