### F or printing ABCDE  pattern ###
num=65
for i in range(1,6):
    for j in range(1,6):
        print(chr(num), end="")
    print()
    num=num+1

### for printing them reverse order ###
num = 69

for i in range(1, 6):
    for j in range(1, 6):
        print(chr(num), end="")
    print()
    num = num - 1