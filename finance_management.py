from random import randint
y = 0 

income = int(input("Please enter your income "))
expenses = ["Rent","Groceries","Utility Bills","Entertainment","Emergency"]
budget = income
for i in expenses :
    u = int(input(f"Please enter your {i} expenses "))
    budget = budget - u
x = str(input("Do you have another expense (No , Yes) "))
x = x.lower
if x == "Yes" :
    y = 1
while y == 1 :
    expenses.append(str(input("Please enter your expenses ")))
    i = int(input(f"Please enter your {expenses[-1]} expenses "))
    expenses[expenses[-1]] = i
    budget = budget - i
    x = str(input("Do you have another expense (No , Yes) "))
    if x == "No" :
        y = 0

random_change = randint(-3000,3000)
budget2 = budget + random_change
if 0 in expenses:
    expenses.remove(0)

print("Yor finance management is:")
print(f"Your income is {income}")
print(f"Your expenses are {expenses}")
print(f"Your budget is {budget}")
print("*************")
print(f"Your random change is {random_change}")
print(f"Your new budget is {budget2}")

