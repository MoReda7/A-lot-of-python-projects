print("celsius to ferenheit (1)")
print("ferenheit to celsius (2)")
x = int(input("Enter your choose: "))

if x == 1:
    # celsius to farenheit
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"the temperature in farenheit : {fahrenheit}")
elif x== 2:
    #fahrenheit to celsius
    fahrenheit2 = float(input("Enter temperature in fahrenheit: "))
    celsius2 = (fahrenheit2 - 32) * 5/9
    print(f"the temperature in celsius : {celsius2}")
else:
    print("Invalid input")