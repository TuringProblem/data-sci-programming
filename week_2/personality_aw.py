##################################
## Author: Andrew               ##
##******************************##
## result = year_of_birth - 4   ##
## another_result = result % 12 ##
## (should be in range 0 - 11)  ##
##################################
personality_list = {
    0: "Beagle",
    1: "Poodle",
    2: "Golden Retriever",
    3: "Dachshund",
    4: "Dalmatian",
    5: "Pointer",
    6: "German Shepherd",
    7: "Portuguese Water Dog",
    8: "Labrador Retriever",
    9: "Yorkie",
    10: "Old English Sheepdog",
    11: "Bulldog",
}

birthyear = int(input("Please enter your year of birth: "))
result = birthyear - 4
handler = lambda x: x % 12

print(
    f"Birth year: {birthyear}\nYour personality is: {personality_list[handler(result)]}"
)
