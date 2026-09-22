# finding 2nd largest number in list 
numbers=[10,45,23,67,89,69]
unique_numbers=list(set(numbers))
unique_numbers.sort()
print("2nd largest number:",unique_numbers[-2])