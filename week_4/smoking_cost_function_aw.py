####################
## Author: Andrew ##
##****************##

## I'm actually shocked how nice this turned out to be...
## essentially I'm taking the sum of c or COST (as a const) and y or YEAR ->
## and for each year I take the cost plus + .10 (fixed rate of cost increase) * the years
## This (c + 0.10 * year) is in parenthesis due to the for loop within the lambda expression
## This allows for year 1 cost would just be 1.10 -> 2 == 1.20 ... and then * 365

calc_total = lambda c, y, p: sum(
    ((c * (0.10 + 1) ** year) * p) * 365 for year in range(y)
)
ex_cost_one = 1
y_one = 2
exOnePpd = 1
exTwoPpd = 3
ex_cost_two = 12
y_two = 30

total_one = calc_total(ex_cost_one, y_one, exOnePpd)
total_two = calc_total(ex_cost_two, y_two, exTwoPpd)
print(f"Example one return: {total_one}\nExample two return: {total_two}")
