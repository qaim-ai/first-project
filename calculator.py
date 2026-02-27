num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose an operation:")
print("a. Addition")
print("b. Subtraction") 
print("c. Multiplication")
print("d. Division")

choice = input("Enter your choice (a/b/c/d): ").lower()
if choice == "a":
    result = num1 + num2
    print("Result:", result) 

elif choice == "b":
    result = num1 - num2
    print("Result:", result)

elif choice == "c": 
    result = num1 * num2
    print("Result:", result)
    
elif choice == "d":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("Result:", result)
