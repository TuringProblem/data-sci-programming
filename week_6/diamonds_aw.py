####################
## Author: Andrew ##
##****************##

import csv

#[2] cut

data = {
        'Ideal': 0,
        'Fair': 0,
        'Good': 0,
        'Very Good': 0,
        'Premium': 0
        }
 
#Diamonds are rated by a number of attributes.  One of those ratings is cut.  -> i[2]

#To determine the possible cut ratings noted in the file you must first find the unique values in the index position 2 (i.e. [2]).

#In this assignment you are to determine and output to the screen the number of diamonds in each cut rating.  Hint: use the set method. Hint: there are 5 ratings.

# Unique
uCuts = set()

with open("Diamonds_Dataset.csv", mode='r') as iFile:
    reader = csv.reader(iFile)
    next(reader)

    for i in reader:
        cut = i[2]
        uCuts.add(cut)

        if cut in data:
            data[cut] += 1



print("Diamond Cut Counts:")
print("-" * 30)
print(f"\nUnique cut values found in data: {uCuts}\nCount of diamonds by cut rating:")
for cut, count in data.items():
    print(f"{cut}: {count:,} diamonds")
        
        

 
