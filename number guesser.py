import random
x = random.randint(1,100)
y = 0
a = 0
for i in range(10):
    z = int(input("Enter a number between (1-100)"))
    y += 1
    if z > x:
        print("your number is too high")
    elif z < x:
        print("your number is too low")
    else:
        print(f"{z} is the correct number")
        print(f"it took you {y} times to guess the number")
        a = 1
        break

if a == 0:
    print("GAME OVER!")