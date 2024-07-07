def perform_operation(num1, num2, operation):
   ##check for the arithmetic operation to execute
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print("input a valid operation")
        return num1 / num2
    else:
        raise ValueError(f"Unsupported operation: {operation}")
