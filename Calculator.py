import math
import datetime
from datetime import datetime

calc_history =[]

def add(x, y):
    return x + y

def power(x, y):
    if y == 0:
        return 1
    return x ** y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def square_root(x):
    if x < 0:
        return "Error! Can't get square root."
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Error! Can't get the factorial."
    return math.factorial(int(x))

# calculation function
def calculations():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply.")
    print("4. Divide.")
    print("5. Power.")
    print("6. Sqrt.")
    print("7. Factorial.")
    print("8. View History.")
    print("9. Exit.")

#Last five calculation history
def history(*args):
    if args:
        calc_history.append(args)
    if len(calc_history) > 5:
        calc_history.pop(0)
    return calc_history[-5:]

#save calculation to a file
def save_to_file(**kwargs):
    filename = kwargs.get("filename", "calculations.txt")
    with open(filename, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}): {kwargs.get('calculations')}\n")
    print(f"calculations saved to {filename}")

# Take input from the user
dec = input("Choose option (1/2/3/4/5/6/7/8/9): ")
if dec in ['1', '2', '3', '4', '5', '6','7','8','9']:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if dec == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif dec == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif dec == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif dec == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif dec == '5':
        print(math.pow(num1, num2))
    elif dec == "6":
        print(math.sqrt(num1))
    elif dec == "7":
        print(math.factorial(int(num1)))
    elif dec == "8":
        print("Last 5 Calculations:")
        for calc in history():
            print(calc)
    elif dec == "9":
        print("Exiting the calculator.")
        break

else: 
    print("Invalid input")

    calc()