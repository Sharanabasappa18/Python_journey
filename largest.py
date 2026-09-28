nums=[100,357,67,8379,327,38,388,373]
largest=nums[0]

for num in nums:
    if num > largest:
        largest=num
print(largest)