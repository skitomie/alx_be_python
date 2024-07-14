
def safe_divide(numerator, denominator):
    denominator = float(denominator)
    numerator = float(numerator)

    try:
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        else:
         print(f"The result of the Division is: {numerator / denominator}")

    except ValueError:
            print("Enter a number")
    
