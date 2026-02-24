# Check that users have entered a valid
# option based on a list

def string_checker(question, valid_ans=['yes', 'no']):

    error = f"Please enter a valid option from the following list {valid_ans}"

    while True:

        #get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            #check if the user response is a word in the list
            if item == user_response:
                return item

            #check if the user response is the same as
            #the first letter of an item on the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()

# Main routine goes here


rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = string_checker("Do you wish to see the instructions? ")

print("You have chosen:", want_instructions)

user_choice = string_checker("Choose: ", rps_list)
print("You have selected:", user_choice)
