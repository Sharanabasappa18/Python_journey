###finding 2nd largest number in list ###
numbers=[10,45,23,67,69,10,89,69]
numbers.append(45)
print(numbers)
unique_numbers=list(set(numbers))
unique_numbers.sort()
print("2nd largest number:",unique_numbers[-2])
print("Sorted list:",unique_numbers)

###finding even & odd numbers in list ####
even=[]
odd=[]

for num in numbers:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print("Even list :",even)
print("Odd list :",odd)

## finding max ,average & min ##
Max=max(numbers)
Min=min(numbers)
Average=sum(numbers)/len(numbers)
print("Average of the list : ",Average)
print("Maximum: ",Max)
print("Minimum: ",Min)
print("Maximum number index : ",numbers.index(Max))
print("Minimum number index : ",numbers.index(Min))