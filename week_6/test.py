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
cleaned = []

for i in range(len(variables)):
    print(variables[i])
    cleaned.append(variables[i].replace(" ", "_"))
    
print(cleaned)

accounts = {
        123: 100, 
        378: 150,
        482: 100
}
print(accounts[123])
accounts[123] = 15000
print(f"My total balance now: {accounts[123]}")
data = {}
for x in cleaned:
    data[x] = [0, 0, 0]
print(f"\n{data}")


female = 0
csvFile = "TitanicSurvival.csv"
with open(csvFile, mode='r') as iFile:
    reader = csv.reader(iFile)
    for i in reader:
        if i[4] == "1st":
            data['The_percentage_of_1st_class_passengers_who_perished'][0] += 1
            if i[2] == "male":
                data["The_percentage_of_1st_class_male_passengers_who_perished"][2] += 1
            else:
                female += 1
        if i[1] == 'no':
            data['The_percentage_of_1st_class_passengers_who_perished'][1] += 1



print(data)
print(f"female's: {female}")

