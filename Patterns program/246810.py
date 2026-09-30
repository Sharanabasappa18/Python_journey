for i in range(1,6):
    num=2
    for j in range(1,6):
        if j<=i:
            print(num,end="")
            num=num+2
        else:
            print("",end="")
    print()