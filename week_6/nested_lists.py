import random
"""
    @Author: Override
    @Since: 20241030
"""

# empty lists
week = []
day = []

'''
 NOTE:
     - 1 day -> 24 hours
     - 1 week -> 7 days
     fill up the day, and add it to the week
'''
for d in range(7):
    for h in range(24):
        day.append(random.randint(0, 100))
    week.append(day)
    day = []
print(week)


hourlyPatients =  [0] * 24
print(f"{hourlyPatients}")
for d in week:
    for i in range(24):
        hourlyPatients[i] += d[i]

print("______________________________________________________________________________________________")
print(hourlyPatients)

for i in range(10):
    print(i, end="-")
for j in range(10, 20):
    print(j, end="-")

for p in range(10, 20, 4):
    print(p, end="-")

myList = [1, 3, 4, 5]
for number in myList:
    if number == 5:
        continue
    print(number)


myListTwo = list(range(3, 9))

print(f"Second list{myListTwo}")
myListThree = list(range(10, 0, -2))
print(f"Third list{myListThree}")

for day in week:
    print(f"Minimum day: {min(day)}\nMaximum day: {max(day)}\nSum: {sum(day)}")

myList = [value +5 for value in range(10, 20)]
print(myList)

