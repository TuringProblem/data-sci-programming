############
## Andrew ##
##********##
## r -> s ##
## r -> l ##
## s -> p ##
## s -> l ##
## p -> r ##
## p -> k ##
## k -> s ##
## k -> r ##
## l -> k ##
## l -> p ##
############
import random;

possible_variants = [ 'R', 'P', 'S', 'L', 'K' ];

possible_outcomes = {
        'r': ['s', 'l'],
        's': ['p', 'l'], 
        'p': ['r', 'k'],
        'k': ['s', 'r'],
        'l': ['k', 'p']
        };

def handle_outcome():
    while True:
        computer_answer = random.choice(possible_variants).lower();
        user_input = input("Please enter r, p, s, l, or k: ");
        if len(user_input) != 1:
            print("Invalid amound, please enter one character!\n");
            continue
        user_answer = user_input[0]; #represents the char value
        
        if user_answer not in possible_variants: #Checking if the value is valid or not :P
            print("Error: cannot find value\n");
        else:
            break;

        #Handle each case, if equal, if won, if lose
        if user_input == computer_answer:
            return f"[TIE]\nComputer Answer: {computer_answer}\nYour Answer: {user_answer}";
        if computer_answer in possible_outcomes[user_answer]:
            return f"[YOU WIN!!]\nYour Answer: {user_answer}\nComputer Answer: {computer_answer}";
        else:
            return f"[YOU LOSE]\nComputer Answer: {computer_answer}\nYour answer: {user_answer}";

print(handle_outcome());
