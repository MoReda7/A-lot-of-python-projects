def basic_salary(hour_rate , hours_worked):
    return hour_rate * hours_worked
def bonus(hour_rate , hours_worked):
    return hour_rate * hours_worked
def total_salary(basic_salary , bonus):
    return basic_salary + bonus

x = int(input("put the hour rate "))
y = int(input("put the hours worked "))

if y <= 40:
    a = basic_salary(x,y)
    print(a)
else:
    z = int(input("put the overtime hour rate "))
    a = basic_salary(x,40)
    b = bonus(z,y-40)
    c = total_salary(a,b)
    print(c)