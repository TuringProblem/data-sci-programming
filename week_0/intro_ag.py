'''
@author: @Override
@since: 09/06/2024
'''''
import time

def lazyLoader(partial):
    print("|.      |\n")
    time.sleep(0.1)
    print("|..     |\n")
    time.sleep(0.3)
    print("|...    |\n")
    time.sleep(0.5)
    print("|....   |\n")
    if partial:
        return ""
    time.sleep(0.6)
    print("|.....  |\n")
    time.sleep(2)
    print("|...... |\n")
    time.sleep(3)
    return "|.......|\n"

def introuction():
    print("Sending POST request...\n")
    time.sleep(2)
    print(lazyLoader(partial = False))
    print("Data received: 127.01.01\n")
    print(lazyLoader(partial = False))
    print("Collecting Andrew's profile information...\n")
    print("\n\n\n")
    time.sleep(2)

    print("H   H  EEEEE  L      L       OOO\n")
    time.sleep(0.2)
    print("H   H  E      L      L      O   O\n") 
    time.sleep(0.2)
    print("HHHHH  EEEE   L      L      O   O\n") 
    time.sleep(0.2)
    print("H   H  E      L      L      O   O\n") 
    time.sleep(0.2)
    print("H   H  EEEEE  LLLLL  LLLLL   OOO\n\n\n\n") 
    time.sleep(2)    
    print("My name is Andrew, I am a Computer Science student at Massasoit. I am currently taking four courses this semester: American Literature, Calculus I, Computer Architecture, and Data Sci Programming I."
            + "I am expected to graduate this spring, and hope to attend NorthEastern or MIT.\nI am taking this course to extend my knownledge in Data types/Structures and also to learn python.")
    return

def seeYa(name):
    print("Gathering response...\n")
    time.sleep(3)
    print(lazyLoader(partial = True))
    time.sleep(2)
    print("+---------------------------+\n")
    print("|         ERROR!             |\n")
    print("|----------------------------|\n")
    print("| An unexpected issue has    |\n")
    print(f"| {name.upper()} is not a   |\n") 
    print("valid response.              |\n")
    print("+---------------------------+\n")
    return "Goodbye" 


isName = lambda name: introuction() if name.lower() == "yes" else seeYa(name) 
userInput = input("Are you Professor Brown-SederBerg?\nPlease respond with EITHER yes, or no: \n\n")
print(isName(userInput))
