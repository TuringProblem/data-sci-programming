import itertools

#############
## Author: Andrew ##
##****************##
## You have a number of stocks. You have decided to determine how much money
## you will have after you sell all of your stocks and pay the taxes.
## The following list details your stocks. Each line details the purchase price, sales price,
## time pf period held ('L' indicates long-term and 'S' indicates sort-term).


## Short-term stocks are held one year or less
## Long-term stocks are held more than one year
## Short-term gains will be taxed at 22% -> .22
## Long-term gains will be taxed at 15% -> .15


stocks = [
    [15000, 11500, "S"],
    [15000, 25100, "L"],
    [30000, 21000, "L"],
    [15000, 50000, "S"],
    [5000, 21000, "S"],
    [25000, 40000, "L"],
    [10000, 10500, "S"],
    [20000, 11000, "S"],
    [30000, 11500, "S"],
    [30000, 11500, "L"],
    [15000, 45000, "L"],
    [15000, 25100, "S"],
    [35000, 50000, "S"],
    [25000, 30000, "L"],
    [30000, 45000, "S"],
]


lTerm = list(itertools.filterfalse(lambda x: x[2] == "S", stocks))
sTerm = list(itertools.filterfalse(lambda x: x[2] == "L", stocks))

print(f"\n\n\nMy Long-term: {lTerm}\n\n\n\n")
print(f"\n\n\nMy Short-term: {sTerm}\n\n\n\n")


def handleTerms(val):
    gainsWithLoses = []
    for s in val:
        dif = s[1] - s[0]
        gainsWithLoses.append(dif)
        print(gainsWithLoses)

    loss = []
    if val == lTerm:
        newAmount = list(itertools.dropwhile(lambda x : x > 0, gainsWithLoses))
        print(f"\n\n\nshit{newAmount}\n\n\n")
        for i in gainsWithLoses:
            if i < 0:
                continue

            loss.append(i)
            gainsWithLoses.remove(i)
        return  gainsWithLoses
    else:
        for j in gainsWithLoses:
            if j < 0:
                continue
            loss.append(j)
            gainsWithLoses.remove(j)
        print(f"Gains (After the negatives are out): {gainsWithLoses}")
        return gainsWithLoses

print(f"\n\nShort-term: {handleTerms(sTerm)}\t\nLong-term: {handleTerms(lTerm)}\n\n")


sNums = [n for s in sTerm for n in s[:2]]
lNums = [n for s in lTerm for n in s[:2]]

print(f"Long-term Values: {sNums}\nLong-term Values: {lNums}\n\n")
print(f"Short-term (before calculations): {sTerm}\n\n")




print(f"{handleTerms(sTerm)}\n{handleTerms(lTerm)}")
## You are to calculate and print to the screen the following:

## - total long term gains/losses


## - total short term gains/lossed

## - Amount of tax you will pay on total long-term gains (you do not pay taxes on losses)


## - Amount of tax you will pay on total short-term gains (you do not pay taxes on losses)


## - Amount of tax you will have after you sell all of your stocks and pay the taxes due
