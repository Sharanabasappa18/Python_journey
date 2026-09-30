num=1
for i in range(1,6):
    k=num
    for j in range(1,6):
        if j<=i:
            print(k,end="")
            k=k+2
        else:
            print("",end="")
    print()
    num=num+2