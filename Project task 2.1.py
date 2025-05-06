services = [
    'اصدار رخصة سيارة اول مرة',
    'تجديد رخصة سيارة',
    'اصدار رخصة قيادة اول مرة',
    'تجديد رخصة قيادة',
    'اصدار بدل فاقد'
]
new_car_id = [
    ["13-04-2025", "Sunday",    [4, 6, 7, 8, 1]],
    ["14-04-2025", "Monday",    [2, 1, 8, 6, 4]],
    ["15-04-2025", "Tuesday",   [3, 1, 6, 6, 4]],
    ["16-04-2025", "Wednesday", [1, 6, 9, 8, 3]],
    ["17-04-2025", "Thursday",  [4, 7, 7, 10, 1]]
]

renew_car_id = [
    ["13-04-2025", "Sunday",    [4, 9, 7, 7, 1]],
    ["14-04-2025", "Monday",    [3, 1, 7, 7, 3]],
    ["15-04-2025", "Tuesday",   [3, 5, 9, 10, 2]],
    ["16-04-2025", "Wednesday", [3, 6, 6, 9, 1]],
    ["17-04-2025", "Thursday",  [1, 2, 9, 8, 4]]
]

new_driving_license = [
    ["13-04-2025", "Sunday",    [2, 4, 9, 6, 2]],
    ["14-04-2025", "Monday",    [2, 6, 8, 8, 1]],
    ["15-04-2025", "Tuesday",   [4, 5, 6, 8, 2]],
    ["16-04-2025", "Wednesday", [3, 10, 6, 10, 1]],
    ["17-04-2025", "Thursday",  [2, 5, 10, 6, 2]]
]

renew_driving_license = [
    ["13-04-2025", "Sunday",    [2, 6, 10, 8, 4]],
    ["14-04-2025", "Monday",    [1, 3, 7, 7, 4]],
    ["15-04-2025", "Tuesday",   [2, 6, 10, 6, 1]],
    ["16-04-2025", "Wednesday", [2, 10, 7, 8, 1]],
    ["17-04-2025", "Thursday",  [2, 7, 7, 7, 1]]
]

lost_id = [
    ["13-04-2025", "Sunday",    [1, 3, 9, 8, 3]],
    ["14-04-2025", "Monday",    [3, 9, 6, 6, 4]],
    ["15-04-2025", "Tuesday",   [4, 7, 8, 7, 3]],
    ["16-04-2025", "Wednesday", [3, 9, 6, 9, 4]],
    ["17-04-2025", "Thursday",  [2, 4, 10, 7, 1]]
]

def mean(data):
  books = [slot for day in data for slot in day[2]]
  return sum(books) / len(books)

def most_crowded_day(data):
  books = [(sum(day[2]),day[1]) for day in data]
  return max(books)

def least_crowded_day(data):
  books = [(sum(day[2]),day[1]) for day in data]
  return min(books)

while True:
  print("Hello! How can I serve you")
  print("1.Mean")
  print("2.Most crowded day")
  print("3.Least crowded day")
  choose1 = int(input())
  print("Choose the service")
  print("1.New car ID")
  print("2.Renew car ID")
  print("3.New driving liscense")
  print("4.Renew driving liscense")
  print("5.Lost ID")
  choose2 = int(input())

  if choose1 == 1:
    if choose2 == 1:
      v1 = mean(new_car_id)
      print(v1)
    elif choose2 == 2:
      v2 = mean(renew_car_id)
      print(v2)
    elif choose2 == 3:
      v3 = mean(new_driving_license)
      print(v3)
    elif choose2 == 4:
      v4 = mean(renew_driving_license)
      print(v4)
    elif choose2 == 5:
      v5 = mean(lost_id)
      print(v5)
    else:
      print("Invalid input")
  elif choose1 == 2:
    if choose2 == 1:
      v1 = most_crowded_day(new_car_id)
      print(v1)
    elif choose2 == 2:
      v2 = most_crowded_day(renew_car_id)
      print(v2)
    elif choose2 == 3:
      v3 = most_crowded_day(new_driving_license)
      print(v3)
    elif choose2 == 4:
      v4 = most_crowded_day(renew_driving_license)
      print(v4)
    elif choose2 == 5:
      v5 = most_crowded_day(lost_id)
      print(v5)
    else:
      print("Invalid input")
  elif choose1 == 3:
    if choose2 == 1:
      v1 = least_crowded_day(new_car_id)
      print(v1)
    elif choose2 == 2:
      v2 = least_crowded_day(renew_car_id)
      print(v2)
    elif choose2 == 3:
      v3 = least_crowded_day(new_driving_license)
      print(v3)
    elif choose2 == 4:
      v4 = least_crowded_day(renew_driving_license)
      print(v4)
    elif choose2 == 5:
      v5 = least_crowded_day(lost_id)
      print(v5)
    else:
      print("Invalid input")
  else:
    print("Invalid input")
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