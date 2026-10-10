num = 153
t = num
sum = 0

while num > 0:
    ld = num % 10
    sum = sum + ld * ld * ld
    num = num // 10

print("Original number:", t)
print("Armstrong sum:", sum)

if t == sum:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")