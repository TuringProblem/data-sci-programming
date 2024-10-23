mylist = []
my_dog = ["Bella", 7, "GR", True]


n = len(my_dog)
print(f"Lenght: {len(my_dog)}")


print(f"\nn: {n}\n")

print(f"n-1: {my_dog[n - 1]}\n")


print(my_dog, sep="-", end=" " + "\n")


for i in my_dog:
    print(f"{i}\n")

# An empty list
daily_numbers = []


numbs = list(range(5, 25))
print(numbs, end="\n")

for i in numbs:
    if numbs[i] % 2:
        print(f"Even!!!! {i}")


# --------------------------- First class lesson below


for num in range(10):
    mylist.append(num)
    print(mylist)

mylist[2] = 99
print(mylist)

mylist_two = [3, 4, "Hello", 9.2]
mylist_three = [0] * 5
