import os
import math
import pyfiglet

def add(x, y):
    explanation = f"The sum of {x} and {y} is {x + y}."
    return x + y, explanation

def subtract(x, y):
    explanation = f"The difference between {x} and {y} is {x - y}."
    return x - y, explanation

def multiply(x, y):
    explanation = f"The product of {x} and {y} is {x * y}."
    return x * y, explanation

def divide(x, y):
    if y == 0:
        return "Error! Division by zero.", "Cannot divide by zero."
    else:
        explanation = f"{x} divided by {y} gives {x / y}."
        return x / y, explanation

def exponentiation(x, y):
    explanation = f"{x} raised to the power of {y} gives {x ** y}."
    return x ** y, explanation

def square_root(x):
    if x < 0:
        return "Error! Imaginary result.", "Cannot calculate square root of a negative number."
    else:
        explanation = f"The square root of {x} is {math.sqrt(x)}."
        return math.sqrt(x), explanation

def factorial(x):
    explanation = f"The factorial of {x} is {math.factorial(x)}."
    return math.factorial(x), explanation

def absolute(x):
    explanation = f"The absolute value of {x} is {abs(x)}."
    return abs(x), explanation

def natural_log(x):
    if x <= 0:
        return "Error! Undefined result.", "Natural logarithm is undefined for non-positive numbers."
    else:
        explanation = f"The natural logarithm of {x} is {math.log(x)}."
        return math.log(x), explanation

def log_base_10(x):
    if x <= 0:
        return "Error! Undefined result.", "Logarithm base 10 is undefined for non-positive numbers."
    else:
        explanation = f"The logarithm base 10 of {x} is {math.log10(x)}."
        return math.log10(x), explanation

def sin(x):
    explanation = f"The sine of {x} radians is {math.sin(x)}."
    return math.sin(x), explanation

def cos(x):
    explanation = f"The cosine of {x} radians is {math.cos(x)}."
    return math.cos(x), explanation

def tan(x):
    explanation = f"The tangent of {x} radians is {math.tan(x)}."
    return math.tan(x), explanation

def radians_to_degrees(x):
    explanation = f"{x} radians is equal to {math.degrees(x)} degrees."
    return math.degrees(x), explanation

def degrees_to_radians(x):
    explanation = f"{x} degrees is equal to {math.radians(x)} radians."
    return math.radians(x), explanation

def calculate_percentage(numerator, denominator):
    if denominator == 0:
        return "Error! Division by zero.", "Cannot calculate percentage with denominator zero."
    else:
        percentage = (numerator / denominator) * 100
        explanation = f"{numerator} out of {denominator} is {percentage}%."
        return percentage, explanation

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        ascii_banner = pyfiglet.figlet_format("Crumbulator")
        print(ascii_banner)
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiation")
        print("6. Square Root")
        print("7. Factorial")
        print("8. Absolute Value")
        print("9. Natural Logarithm (ln)")
        print("10. Logarithm Base 10 (log10)")
        print("11. Sine")
        print("12. Cosine")
        print("13. Tangent")
        print("14. Convert Radians to Degrees")
        print("15. Convert Degrees to Radians")
        print("16. Calculate Percentage")
        print("0. Exit")

        choice = input("Enter choice (0-16): ")

        if choice == '0':
            print("Exiting...")
            break
        elif choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result, explanation = add(num1, num2)
            elif choice == '2':
                result, explanation = subtract(num1, num2)
            elif choice == '3':
                result, explanation = multiply(num1, num2)
            elif choice == '4':
                result, explanation = divide(num1, num2)
        elif choice == '5':
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            result, explanation = exponentiation(base, exponent)
        elif choice == '6':
            num = float(input("Enter the number: "))
            result, explanation = square_root(num)
        elif choice == '7':
            num = int(input("Enter the number: "))
            result, explanation = factorial(num)
        elif choice == '8':
            num = float(input("Enter the number: "))
            result, explanation = absolute(num)
        elif choice == '9':
            num = float(input("Enter the number: "))
            result, explanation = natural_log(num)
        elif choice == '10':
            num = float(input("Enter the number: "))
            result, explanation = log_base_10(num)
        elif choice == '11':
            angle = float(input("Enter the angle in radians: "))
            result, explanation = sin(angle)
        elif choice == '12':
            angle = float(input("Enter the angle in radians: "))
            result, explanation = cos(angle)
        elif choice == '13':
            angle = float(input("Enter the angle in radians: "))
            result, explanation = tan(angle)
        elif choice == '14':
            radians = float(input("Enter the angle in radians: "))
            result, explanation = radians_to_degrees(radians)
        elif choice == '15':
            degrees = float(input("Enter the angle in degrees: "))
            result, explanation = degrees_to_radians(degrees)
        elif choice == '16':
            numerator = float(input("Enter the numerator: "))
            denominator = float(input("Enter the denominator: "))
            result, explanation = calculate_percentage(numerator, denominator)
        else:
            print("Invalid input")
            continue

        print("Result:", result)
        print("Explanation:", explanation)

        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
