###finding 2nd largest number in list ###
numbers=[10,45,23,67,89,69]
# unique_numbers=list(set(numbers))
# unique_numbers.sort()
# print("2nd largest number:",unique_numbers[-2])

###finding even & odd numbers in list ####
even=[]
odd=[]

for num in numbers:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print("Even:",even)
print("Odd:",odd)