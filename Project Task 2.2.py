new_car_id = [
    ["18-04-2025", "Sunday",    [6, 10, 1, 10, 7]],
    ["19-04-2025", "Monday",    [10, 2, 10, 6, 4]],
    ["20-04-2025", "Tuesday",   [3, 1, 10, 10, 9]],
    ["21-04-2025", "Wednesday", [10, 8, 10, 7, 3]],
    ["22-04-2025", "Thursday",  [2, 10, 4, 10, 1]]
]

renew_car_id = [
    ["18-04-2025", "Sunday",    [9, 8, 7, 10, 10]],
    ["19-04-2025", "Monday",    [2, 9, 10, 3, 10]],
    ["20-04-2025", "Tuesday",   [1, 1, 10, 9, 10]],
    ["21-04-2025", "Wednesday", [10, 3, 9, 10, 9]],
    ["22-04-2025", "Thursday",  [10, 5, 2, 10, 3]]
]

new_driving_license = [
    ["18-04-2025", "Sunday",    [10, 2, 10, 4, 1]],
    ["19-04-2025", "Monday",    [3, 10, 4, 10, 5]],
    ["20-04-2025", "Tuesday",   [9, 10, 2, 6, 10]],
    ["21-04-2025", "Wednesday", [10, 3, 10, 5, 7]],
    ["22-04-2025", "Thursday",  [2, 10, 4, 6, 10]]
]

renew_driving_license = [
    ["18-04-2025", "Sunday",    [10, 4, 5, 10, 1]],
    ["19-04-2025", "Monday",    [5, 6, 10, 3, 10]],
    ["20-04-2025", "Tuesday",   [10, 8, 1, 3, 10]],
    ["21-04-2025", "Wednesday", [2, 9, 10, 10, 6]],
    ["22-04-2025", "Thursday",  [10, 7, 4, 10, 3]]
]

lost_id = [
    ["18-04-2025", "Sunday",    [9, 10, 10, 9, 1]],
    ["19-04-2025", "Monday",    [3, 10, 4, 10, 4]],
    ["20-04-2025", "Tuesday",   [2, 9, 6, 10, 10]],
    ["21-04-2025", "Wednesday", [6, 10, 5, 10, 2]],
    ["22-04-2025", "Thursday",  [9, 10, 4, 10, 4]]
]

users = {}

services = ["New car ID", "Renew car ID", "New driving license", "Renew driving license", "Lost ID"]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
dates = ["18-04-2025", "19-04-2025", "20-04-2025", "21-04-2025", "22-04-2025"]
times = ["9:00 AM","10:00 AM","11:00 AM","12:00 AM","1:00 PM"]

service_datasets = [new_car_id, renew_car_id, new_driving_license, renew_driving_license, lost_id]

def app():
  print("Welcome to Auroriva's Booking managment subsystem")
  print("Choose a service:")
  print("1.New car ID")
  print("2.Renew car ID")
  print("3.New driving license")
  print("4.Renew driving license")
  print("5.Lost ID")
  choose2 = int(input("Enter your choose here! "))
  while choose2 < 1 or choose2 > 5:
    print("Invalid input. Please try again.")
    choose2 = int(input("Enter your choose here! "))
  print("Choose the day:")
  print("1.Sunday, 18-04-2025")
  print("2.Monday, 19-04-2025")
  print("3.Tuesday, 20-04-2025")
  print("4.Wednesday, 21-04-2025")
  print("5.Thursday, 22-04-2025")
  choose3 = int(input("Enter your choose here! "))
  while choose3 < 1 or choose3 > 5:
    print("Invalid input. Please try again.")
    choose3 = int(input("Enter your choose here! "))

  selected_data = service_datasets[choose2-1][choose3-1][2]
  available_slots = [10 - res for res in selected_data]

  print("Available time slots:")
  i = 1
  for j in range(len(times)):
      if available_slots[j] > 0:
          print(f"{i}. {times[j]} ({available_slots[j]} available)")
      i = i + 1

  choose4 = int(input("Enter your choose here! "))

  while choose4 < 1 or choose4 > 5 or available_slots[choose4 - 1] <= 0:
    print("Invalid input. Please try again.")
    choose4 = int(input("Enter your choose here! "))

  print("Enter full name:")
  name = input()
  print("Enter Visa card number:")
  card = int(input())

  print("\nReservation Confirmation:")
  print(f"Name: {name}")
  print(f"Visa Card: {card}")
  print(f"Service: {services[choose2-1]}")
  print(f"Date: {dates[choose3-1]}")
  print(f"Day: {days[choose3-1]}")
  print(f"Time: {times[choose4-1]}")

while True:
  print("Welcome to Auroriva's Booking managment subsystem")
  print("1.Login")
  print("2.Sign up")
  print("3.Exit")
  choose1 = int(input("Enter your choose here! "))

  if choose1 == 1:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
      print("Login successful!")
      app()
      x = 0
      while x == 0:
        print("Do you want to exit?")
        print("1.Yes")
        print("2.No")
        choose3 = int(input())
        if choose3 == 1:
          x = 1
        elif choose3 == 2:
          x = 2
        else:
          print("Invalid input")
      if x == 1:
        break
    else:
      print("Invalid username or password. Please try again.")

  if choose1 == 2:
    y = 0
    while y == 0:
      username = input("Enter your username: ")
      print("Hint: the password should contain small and capital letters, should be more than 8 characters, should contain sympols and at least one sympol")
      password = input("Enter your password: ")
      if username in users:
        print("Username already exists. Please choose a different username.")
      elif len(password) < 8:
        print("Password must be at least 8 characters long.")
      elif not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
      elif not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
      elif not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
      elif not any(char in "!@#$%^&*()_+-=[]{}|;':\",./<>?" for char in password):
        print("Password must contain at least one symbol (!@#$%^&*()_+-=[]{}|;':\",./<>?).")
      else:
        users[username] = password
        print("Sign up succesful")
        y = 1
      app()
      x = 0
      while x == 0:
        print("Do you want to exit?")
        print("1.Yes")
        print("2.No")
        choose3 = int(input())
        if choose3 == 1:
          x = 1
        elif choose3 == 2:
          x = 2
        else:
          print("Invalid input")
      if x == 1:
        break
  elif choose1 == 3:
    break
  else:
    print("Invalid input. Please try again.")