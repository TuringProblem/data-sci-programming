##################################################
## for ith month increase infection             ## 
##**********************************************##
## input -> population                          ##
##**********************************************##
## 1st month 10% uninfected -> infected         ##
## 2nd month 15% remaininguninfected -> infected##
## .                                            ##
## .                                            ##
## .                                            ##
## 6th month 35% uninfected -> infected         ##
##################################################

population = int(input("Please enter the population: "))
infection = [10, 15, 20, 25, 30, 35]
infectious = lambda a, b : a * b / 100
total_infected = 0
normies = population

months = 6

for i in range(months):
    zombies = int(infectious(normies, infection[i]))
    print("Total infected for month {}: {:.1f}".format(i + 1, float(zombies)))
    total_infected += zombies
    normies -= zombies

print("Total Infected: {:.1f}".format(total_infected))
print("Total uninfected: {:.1f}".format(normies))

