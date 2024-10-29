ducks = ["Jack", "Kack", "Lack", "Mack", "Nack", "Oack", "Pack", "Qack"]
print(ducks)
ducks.sort()
print(ducks)

ducks.append("Uack")
print(ducks)

corner = ducks.pop(5)
print(corner)

print(ducks)
# ducks.append(corner)
# print(ducks)


ducks.insert(2, "Vack")
print(ducks)

ducks.sort(reverse=True)
print(ducks)

ducks.insert(2, corner)
print(ducks)

ducks.append("Xack")
print(ducks)

p = ducks.index("Uack")
print(f"Index={p}")
del ducks[1]
print(f"After deleting 'Uack' = {ducks}\n")

time_out = last_duck = ducks.pop()
print(f"Deleted the last duck: {time_out}\n")

del ducks[ducks.index("Vack")]
print(f"After kicking out Vack: {ducks}\n")

ducks.append(time_out)
print(ducks)


del ducks[ducks.index("Xack")]
print(ducks)

print(f"Lenghth of new list: {len(ducks)}\n")


ducks.sort()
print(ducks)


ducks.append("Andrew")
print(ducks)
