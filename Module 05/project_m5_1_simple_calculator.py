def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def modulus(x, y):
    return x % y


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

choice = input("Enter choice (1/2/3/4/5): ")
x = input("Enter first number: ")
y = input("Enter second number: ")

try:
    x = float(x)
    y = float(y)
    if choice == '1':
        print(f"{x} + {y} = {addition(x, y)}")
    elif choice == '2':
        print(f"{x} - {y} = {subtraction(x, y)}")
    elif choice == '3':
        print(f"{x} * {y} = {multiplication(x, y)}")
    elif choice == '4':
        print(f"{x} / {y} = {division(x, y)}")
    elif choice == '5':
        print(f"{x} % {y} = {modulus(x, y)}")
    else:
        print("Invalid input. Please try again.")
except Exception as e:
    print(f"Error: {e}")