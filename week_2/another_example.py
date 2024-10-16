n = input("Enter scheduled arrival time: ")
while int(n) < 0 or int(n) > 2359 or int(n) % 100 > 59 or len(n) < 4:
    n = input("Enter scheduled arrival time: ")
    print(n)

d = input("Enter scheduled arrival time: ")
while int(d) < 0 or int(d) > 2359 or int(d) % 100 > 59 or len(d) < 4:
    d = input("Enter scheduled arrival time: ")
    print(d)
