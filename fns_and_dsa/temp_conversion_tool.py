FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
     global celsius
     celsius = (fahrenheit - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR 
     return celsius

def convert_to_fahrenheit(celsius):
    global fahrenheit
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    return  fahrenheit

temp = input("Enter the temperature to convert:")

if not isinstance((temp), float):
            print("Invalid temperature. Please enter a numeric value.")
else: 
    format = input("Is this temperature in Celsius or Fahrenheit? (C/F):").upper()

if format == "C":
      convert_to_fahrenheit(temp)
      print(f"{temp}°C is {fahrenheit}°F")
elif format == "F":
      convert_to_celsius(temp)
      print(f"{temp}°C is {celsius}°F")
else:
      print("Select a valid unit to convert to!!!")