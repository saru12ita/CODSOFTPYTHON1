# Define a function to perform basic arithmetic operations
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"

# Get user input for two numbers and the desired operation
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    # Call the calculate function and display the result
    result = calculate(num1, num2, operation)
    print(f"Result: {result}")
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
