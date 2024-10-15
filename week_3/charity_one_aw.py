####################
## Author: Andrew ##
##****************##
## Assume that you will have 10,000 customers who will have purchase totals of a randomly generated number
## (a float with two decimal values) between $1.00 and $100.00
## In this assignment you are to write the code that will determine and output the following:
## - If all customers participate how much money will be raised?
## - if customers are 50% likely to participate
## hint: use the cieling of x: the smallest integer greatest than or equal to x.


import math
import random

total_customers = 10_000


def donations(customers):
    max_donation = 0
    half_donation = 0

    for _ in range(customers):
        user_purchases = random.uniform(1.00, 100.00)  # for max and min donations
        rounded_purchase = math.ceil(user_purchases)
        donation = rounded_purchase - user_purchases
        max_donation += donation

        if random.randint(0, 1) == 1:
            half_donation += donation

    return max_donation, half_donation


max_donation, half_donation = donations(total_customers)
print(f"\nMax Participation (100%): ${max_donation:.2f}")
print(f"Half Participation (50%): ${half_donation:.2f}\n")
