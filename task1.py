# 1. Take two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# 2. Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

# 3. Display results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
