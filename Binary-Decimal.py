print("Choose the operation you want to perform:")
print("1. Decimal to Binary")
print("2. Binary to decimal")
x = int(input())

if x == 1:
  y = int(input("Enter the number in Decimal "))
  z = []

  while True:
    if y % 2 == 1:
      z.append(1)
      y = y//2
    elif y % 2 == 0:
      z.append(0)
      y = y//2
    if y == 1:
      z.append(1)
      break
    elif y == 0:
      break

  z = z[::-1]
  a = int(''.join(map(str, z)))
  print(a)
elif x == 2:
  c = int(input("Enter the number in Binary "))

  b = list(map(int, str(c)))
  e = len(b)
  d = []
  for i in b:
    f = e - 1

    if i == 1:
      d.append(2**f)
      e = e - 1
    elif i == 0:
      e = e -1
      continue

  g = 0
  for i in d:
    g += i

  print(g)
else:
  print("Invalid input")