
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


totalLongTermGainsLoss = 0
totalShortTermGainLoss= 0
taxLongTermGains = 0
taxShortTermGains = 0
moneyInMyPockets = 0

for stock in stocks:
    d = stock[1] - stock[0]
    if stock[2] == 'L':
        totalLongTermGainsLoss += d
    else:
        totalShortTermGainLoss += d
print("{:,.2f}\n{:,.2f}".format(totalShortTermGainLoss, totalLongTermGainsLoss))


taxLongTermGains = totalLongTermGainsLoss * .15
taxShortTermGains = totalShortTermGainLoss * .22
moneyInMyPockets = totalLongTermGainsLoss + totalShortTermGainLoss\
                    - taxLongTermGains - taxShortTermGains

print("Money in my pocket: ${:,.2f}".format(moneyInMyPockets))

