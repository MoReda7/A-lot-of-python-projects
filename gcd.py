from math import gcd
x = int(input("Enter the 1st number. "))
y = int(input("Enter the 2nd number. "))
print(gcd(x,y))
z = 0
def gcd2(x,y):
    for i in range(1,x+1):
        if x % i == 0:
            if y % i == 0:
                z = i
    return z
            

if x <= y:
    print(gcd2(x,y))
else:
    print(gcd2(y,x))