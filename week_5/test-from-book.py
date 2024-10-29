## slicing

alist = [1, 2, 4, 6, 9]


def calcMean(alist):
    n = len(alist)
    sum = 0
    for i in range(n):
        sum += alist[i]
    return sum / 2


def calcGrowingAverage(alist, r=2):  ## default typing for r
    result = []
    for i in range(len(alist)):
        sublist = alist[0 : 1 + 1]  ## Slicing the element from 0 to 1
        print(f"Sublist: {sublist}")
        mean = calcMean(sublist)
        print(f"Mean: {mean}")
        result.append(round(mean, r))
    return result


test = [10, 15, 21.1, 9.6, 10.1, 9.9, 9.8, 15.5, 17]

print()

myTestMean = calcMean(test)
print(f"test Mean: {myTestMean}")
print(f"Growing Average: {calcGrowingAverage(test)}")
