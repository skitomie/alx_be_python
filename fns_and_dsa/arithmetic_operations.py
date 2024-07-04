def perform_operation(num1,num2,operation):
    def add(num1,num2):
        return num1 + num2
    def subtract(num1, num2):
        return num1 - num2
    def multiply(num1, num2):
        return num1 * num2
    def divide(num1,num2):
        if num2 != 0:
            return num1/num2
        else:
            print("Enter a valid number")


    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation}")

    return operations[operation](num1, num2)