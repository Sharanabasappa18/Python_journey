try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError:
    print("Cannot divide by zero.")
except (ValueError, TypeError) as e:
    print(f"Invalid input or type: {e}")