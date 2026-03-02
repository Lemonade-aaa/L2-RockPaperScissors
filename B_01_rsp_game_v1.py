# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is more or equal to 1. "

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"
        try:
            # response = int(input("Please enter a integer. "))
            response = int(to_check)

            #checks the number is more than / equal to 1
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
                print(error)


# Main Routine Starts here

# Intialise game variables
mode = "regular"
rounds_played = 0


print("🪨📃✂️ Rock / Paper / Scissors Game ✂️📃🪨")
print()


# Instructions

# Ask the user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like to play good sir/madam? Please press <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:
    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1
    print("Rounds played: ", rounds_played)

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

    print("Number of rounds", num_rounds)

# Game loop ends here

# Game history / statistics area