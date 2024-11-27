#Author: Andrew :)
#In this assignment you are to accept a string from the 
#user and generate and print to the screen a new string 
#that is the second half of the original string concatenated 
#to the first half of the original string. 
#If the original string has an even number of characters the 
#first and second half will be equal in length.  If the original 

def handString(input):
    mid = len(input) // 2

    if (len(input) % 2 != 0):
        mid = mid
    first = input[:mid]
    last = input[mid:]

    return last + first

testies = "123456"
testiess = "1234567"


print(f"First evaluation (before): {testies}\nThis is the second (before): {testiess}\n")

testiess = handString(testiess)
testies = handString(testies)

print(f"First evaluation (after): {testies}\nThis is the second (after): {testiess}\n")
