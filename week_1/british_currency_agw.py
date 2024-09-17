#*******************#
# Author: Andrew W. #
#*******************#
#   @09/17/2024     #
#*******************#
pennies = int(input("Please enter the number of Pennies: "))

def currencyConverter(pennies):

    #using a list, and tuple instead of making it verbose
    currency = [
        ("Pound", 240),
        ("Crown", 60), 
        ("Half-crown", 30),
        ("Florin", 24),
        ("Schilling", 12),
        ("Six-pence", 6),
        ("Three-pence", 3),
        ("penny", 1)
    ]
    
    for name, value in currency:
        # for each iteration: value x -> divide by the number of remaining pennies by the value from currency -- 
                                    # -- then mode pennies by that value, and store the remaining inside penny
        x = pennies // value
        pennies %= value
        print(f"{name}: {x}")

currencyConverter(pennies)



