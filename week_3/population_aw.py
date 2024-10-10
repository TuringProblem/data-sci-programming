####################
## Author: Andrew ##
##****************##
## The popyulation of the US starting is 335,893,238
## pop increase 1.2% every year through births
## pop decrease 0.85% every year through deaths
## The population increase every year 1,125,000 from immigration/emigration


def pop_handler():
    start_pop = 335_893_238
    births = 1.2 / 100
    deaths = 0.85 / 100
    imemgration = 1_125_000
    year = 25
    print(f"{'Year':<10}{'Population':<15}")
    currentpop = start_pop
    for i in range(1, year + 1):
        birthr = currentpop * births
        deathr = currentpop * deaths
        combined_increase = birthr - deathr + imemgration

        currentpop += combined_increase
        print(f"Population: {currentpop:.2f}")


pop_handler()
