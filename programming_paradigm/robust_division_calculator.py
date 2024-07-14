
def safe_divide(numerator, denominator):
    numerator = float(numerator)
    denominator = float(denominator)
    try:
        ans =  numerator/ denominator
        print(f"The result of the division is: {ans}")

    except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
   

    except ValueError:
         print("Error: Please enter numeric values only.")
    
