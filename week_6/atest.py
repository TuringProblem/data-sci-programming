####################
## Author: Andrew ##
##****************##
import csv

variables = [   
    "The percentage of 1st class passengers who perished",
    "The percentage of 2nd class passengers who perished",
    "The percentage of 3rd class passengers who perished",
    "The percentage of 1st class female passengers who perished",
    "The percentage of 1st class male passengers who perished",
    "The percentage of 2nd class female passengers who perished",
    "The percentage of 2nd class male passengers who perished",
    "The percentage of 3rd class female passengers who perished",
    "The percentage of 3rd class male passengers who perished",
]

# I decided to just use two Dictionaries because why not, it's beautiful and easier to read...
data = {
    '1st': {'total': 0, 'perished': 0, 'maleTotal': 0, 'malePerished': 0, 'femaleTotal': 0, 'femalePerished': 0},
    '2nd': {'total': 0, 'perished': 0, 'maleTotal': 0, 'malePerished': 0, 'femaleTotal': 0, 'femalePerished': 0},
    '3rd': {'total': 0, 'perished': 0, 'maleTotal': 0, 'malePerished': 0, 'femaleTotal': 0, 'femalePerished': 0}
}


with open('TitanicSurvival.csv', mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)
    
    for i in reader:
        survived = i[1]
        sex = i[2]
        pClass = i[4]
        
        data[pClass]['total'] += 1
        if survived == 'no':
            data[pClass]['perished'] += 1
            
        if sex == 'male':
            data[pClass]['maleTotal'] += 1
            if survived == 'no':
                data[pClass]['malePerished'] += 1
        else:
            data[pClass]['femaleTotal'] += 1
            if survived == 'no':
                data[pClass]['femalePerished'] += 1

def calculate_percentage(part, whole):
    return (part / whole * 100) if whole > 0 else 0

print("Results:")
for passengerClass in ['1st', '2nd', '3rd']:
    print(passengerClass)

    perishedPercent = calculate_percentage(data[passengerClass]['perished'], data[passengerClass]['total'])
    malePercent = calculate_percentage(data[passengerClass]['malePerished'], data[passengerClass]['maleTotal'])
    femalePercent = calculate_percentage(data[passengerClass]['femalePerished'], data[passengerClass][''])
    print(f"\n{passengerClass} class:\nOverall perished: {perishedPercent:.1f}%\nMale perished: {malePercent:.1f}%\nFemale perished: {femalePercent:.1f}%")
    