x = int(input("put a number "))
if x <= 0:
    print(f"The number {x} isn't a prime number.")
elif x == 1:
    print(f"The number {x} isn't a prime number.")
else:
    def pt(y):
        for i in range(2,y):
            if y % 2 == 0:
                return True

    z = pt(x)
    if z == True:
        print(f"The number {x} isn't a prime number.")
    else:
        print(f"The number {x} is a prime number.")