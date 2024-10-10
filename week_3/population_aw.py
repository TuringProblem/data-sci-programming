####################
## Author: Andrew ##
##****************##
## The popyulation of the US starting is 335,893,238
## pop increase 1.2% every year through births
## pop decrease 0.85% every year through deaths
## The population increase every year 1,125,000 from immigration/emigration

starting_population = 335_893_238


def pop_handler(init_pop, years):
    population = init_pop
    print("Year    Population:")
    for i in range(1, years + 1):
        birthr = int(population * 0.012)  # -> 1.2%
        deathr = int(population * 0.0085)  # -> 0.085%
        imemgration = 1_125_000
        population += birthr - deathr + imemgration
        print(f"{i:<8}{population}")


pop_handler(starting_population, 25)
