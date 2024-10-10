####################
## Author: Andrew ##
##****************##
##If all customers participate how many customers will have to be needed to raise the desired amount?
## If customers are 33% likely to participate how many customers will have to be needed to raise the desired amount? Hint: generate a random number 0, 1, or 3:
## if 0 -> participate
## 1 or 2 -> DO NOT

import math
import random


def donations(prate):
    max_donation = 0
    customers = 0

    while max_donation < 1500:
        purchase_total = random.uniform(1.00, 100.00)
        totalr = math.ceil(purchase_total)
        donation = totalr - purchase_total

        if prate == 1 or (random.randint(0, 2) == 0):
            max_donation += donation

        customers += 1
    return max_donation, customers


full_participation, customers = donations(1)

third_participation, third_customer = donations(0.33)


print(
    f"\nParticipation (100%):\nFunds raised: ${full_participation:.2f}\nCustomers required if participation is 100%: {customers}\n"
)
print(
    f"Participation (33%):\nFunds raised: ${third_participation:.2f}\nCustomers required if participation is 33%: {third_customer}\n"
)
