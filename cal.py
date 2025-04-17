z = None  # Initialize z as None
operator = input("Choose the operator (+, -, *, /, **, ^, //, %): ")

if operator in ["+", "-", "*", "/", "**", "^", "//", "%"]:
    x = int(input("How many numbers do you want to enter? "))
    
    for i in range(x):
        if operator in ["+", "-", "*", "/", "**", "^", "//", "%"]:
            num = int(input(f"Enter number {i + 1}: "))
            
            if z is None:  # First input case
                z = num
            else:
                if operator == "+":
                    z += num
                elif operator == "-":
                    z -= num
                elif operator == "*":
                    z *= num
                elif operator == "/":
                    if num == 0:
                        print("Cannot divide by zero. Please enter a different number.")
                        num = int(input("Enter number again: "))
                    z /= num
                elif operator == "**" or operator == "^":
                    z **= num
                elif operator == "//":
                    if num == 0:
                        print("Cannot divide by zero. Please enter a different number.")
                        num = int(input("Enter number again: "))
                    z //= num
                elif operator == "%":
                    if num == 0:
                        print("Cannot modulo by zero. Please enter a different number.")
                        num = int(input("Enter number again: "))
                    z %= num
            
            print(f"Current result: {z}")
else:
    print("Invalid operator")