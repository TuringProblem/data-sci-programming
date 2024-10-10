# e##################
## Author: Andrew ##
##****************##

import itertools  # # Using this python package, when researching thought it would be unique to add due to it's iterators for "efficient" looping
import math
import operator  # # only using the operator for the .mul func, this function just takes a, b and returns a * b

purchase = float(input("Please enter the purchase price: $"))
years = int(input("Please enter the number of years: "))
affect = []
for i in range(years):
    percent_rate = float(
        input(
            f"Enter the percentage change for year {i + 1}\nExample: 5% == 5\n\nEnter: "
        )
    )
    affect.append(1 + (percent_rate / 100))

product_of_numbers = math.prod(affect)
geomean = product_of_numbers ** (1 / years)

value = purchase * product_of_numbers


print(f"Geometric Mean: ${geomean:.2f}")
print(f"Value of propert after {years} years: ${value:.2f}")

progression = itertools.accumulate(affect, operator.mul)
list = [purchase * val for val in progression]

print("\nYearly Property value: ")
for year, value in enumerate(list, start=1):
    print(f"Year {year}: ${value:.2f}")
