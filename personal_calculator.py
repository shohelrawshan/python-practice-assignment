
#Practice Problem 1: Personal Information & Simple Calculator

name = input("Enter your name:")
age = int(input("Enter your age:"))

num1 = int(input("\nEnter first number:"))
num2 = int(input("Enter second number:"))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

# Display information using f-strings
print(f"\nHello, {name}!")
print(f"Your age is {age}.")
print(f"\n\nAddition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")


