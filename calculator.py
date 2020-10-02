import math

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
yes = input("What would you like to do with these numbers?\n")

if yes == "multiply":
    print(x*y)
elif yes == "add":
    print(x+y)
elif yes == "subtract":
    print(x-y)
elif yes == "divide":
    print(x/y)

input("Press enter to exit.")
