pop = 335_893_238
births = pop / .12
deaths = pop *.085
immagration = 0
year = 0


calculator = lambda x : int((x + births) - (x - deaths) + 1_125_000)

for i in range(25):
    year += 1
    print(f"{year}\t {calculator(pop)}")
                     

##    value = calculator(pop)
##    pop = value
##    print(value)
    i += 1
