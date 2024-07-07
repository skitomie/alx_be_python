
"""
def perform_operation(num1: float,num2: float,operation: str) -> float:
   
   match operation:
      case "add":
         if operation == "add":
            return num1 + num2
      case "subtract":
         if operation == "subtract" :
            return num1 - num2
      case "multiply":
         if operation == "multiply":
            return num1 * num2
      case "divide":
        if operation == "divide" and num2 != 0:
            return num1/num2
        else:
           print("Enter a valid number")

"""

def perform_operation(num1: float, num2: float, operation: str) -> float:
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
