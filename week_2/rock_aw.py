##
##
## r -> s
## r -> l
## s -> p
## s -> l 
## p -> r
## p -> k 
## k -> s 
## k -> r 
## l -> k
## l -> p 
##


import random;

possible_variants = [ 'R', 'P', 'S', 'L', 'K' ];
computer_answer = random.choice(possible_variants).lower()
user_choice = input("Please enter r, p, s, l, or k: ")

def comparitor():
    if (user_choice == computer_answer):
        print("There is a draw!")



    match (user_choice.lower()):
        case 'r':
            if computer_answer == 's' | computer_answer == 'l':
                print("You win bitch!")
            else if computer_answer == 'k' | computer_answer == 'p':
                print("You lose")
            else:
                print("no one win")
        #case 'p':
        

            
print(comparitor())


print(f"Computer answered: {computer_answer}")


