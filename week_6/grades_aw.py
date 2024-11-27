author = """Copyright ℗ 2024 Andrew {@Override} 
      ___          ___         _____         ___          ___          ___     
     /  /\        /__/\       /  /::\       /  /\        /  /\        /__/\    
    /  /::\       \  \:\     /  /:/\:\     /  /::\      /  /:/_      _\_ \:\   
   /  /:/\:\       \  \:\   /  /:/  \:\   /  /:/\:\    /  /:/ /\    /__/\ \:\  
  /  /:/~/::\  _____\__\:\ /__/:/ \__\:| /  /:/~/:/   /  /:/ /:/_  _\_ \:\ \:\ 
 \  \:\/:/__\/\  \:\~~\~~\/ \  \:\  /:/ \  \:\/:::::/\  \:\/:/ /:/\  \:\ \:\/:/
  \  \::/      \  \:\  ~~~   \  \:\/:/   \  \::/~~~~  \  \::/ /:/  \  \:\ \::/ 
   \  \:\       \  \:\        \  \::/     \  \:\       \  \:\/:/    \  \:\/:/  
    \  \:\       \  \:\        \__\/       \  \:\       \  \::/      \  \::/   
     \__\/        \__\/                     \__\/        \__\/        \__\/    
     
"""
import csv
from itertools import accumulate 

iFile = "grade_record.csv"

"""
The file grade_record.csv Download grade_record.csvlists 30,000 grades.  Each line (after the header) has two values [letter grade, numeric grade]. 

Letter grades should be assigned as follows:

Letter          Numeric

A                90 - 100      

B                80 - 89        

C                70 - 79        

D                60 - 69        

F                 < 60:          

The attached file includes errors - specifically letter grades that are incorrect.

Part 1:

In this assignment you are to determine the number and percent of incorrect letter grades.

Name your program grades_percent_part1_your_initials.ipynb, where your_initials represents your initials. 

Part 2:

Building on your work in Part 1 above. Write to a new file (clean_grade_records.csv) of the corrected letter grade and numeric grade (both on the same line) of the letter grade/numeric grade combinations in the file grade_record.csv. Please note the numeric grades remain the same the letter grades may change.

Name your program grades_percent_part2_your_initials.ipynb, where your_initials represents your initials. 
"""

knownGrades = {
    'A': (90, 100), 
    'B': (80, 89),
    'C': (70, 79),
    'D': (60, 69),
    'F': (60)

}
numbers = []
corrected = []

with open(iFile, mode="r") as file:
    reader = csv.reader(file)
    next(reader)
    for i in reader:
        grades = list(i[0])
        print(grades)
        numbers = list(i[1])
        print(numbers)

        
print(numbers)
newNumbers = accumulate(numbers)
print(newNumbers)
        



    
