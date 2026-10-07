a = [2, 45, 6, 7, 2, 3, 56, 78, 9, 0, 2]

for i in range(len(a)):
    for j in range(0, len(a) - i - 1):
        if a[j] > a[j + 1]:
            t = a[j]
            a[j] = a[j + 1]
            a[j + 1] = t

print(a)