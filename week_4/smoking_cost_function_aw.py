####################
## Author: Andrew ##
##****************##

calc_total = lambda c, y: sum((c + 0.10 * year) * 365 for year in range(y))
ex_cost_one = 1
y_one = 2
ex_cost_two = 12
y_two = 30

total_one = calc_total(ex_cost_one, y_one)
total_two = calc_total(ex_cost_two, y_two)
print(total_one)
