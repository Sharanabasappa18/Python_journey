numbers = list(map(int, input("Enter the numbers: ").split()))
n = len(numbers) + 1

expected_sum = n * (n + 1) // 2
missing = expected_sum - sum(numbers)

print("Missing number:", missing)
