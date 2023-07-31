import random

##Generates a random number and returns it
def getNum(digits):
    result = ""
    num = list("0123456789")
    random.shuffle(num)

    for i in range(digits):
        result += num[i]
        
    return(result)

##Compares the user's guess with the secret number and gives a clue
def getClue(guess, secret_num, digits):
    bagel_count = 0
    
    for digit in guess:
        if digit in secret_num:
            if guess.index(digit) == secret_num.index(digit):
                print("Fermi ", end = "")
            elif guess.index(digit) != secret_num.index(digit):
                print("Pico ", end = "")
        else:
            bagel_count += 1

    if bagel_count == digits:
        print("Bagels ", end = "")

    print()
            
def main():
    digits = 0
    max_guesses = 0
    while digits < 1 and max_guesses < 1:
        if digits < 1:
            print("How many digits should the code have?")
            digits = int(input(">"))
            if digits < 1 or digits > 10 or not str(digits).isnumeric:
                print("The code must be between 1-10 digits.")
                digits = 0

        if max_guesses < 1:
            print("How many guesses should you get?")
            max_guesses = int(input(">"))
            if max_guesses < 1 or not str(max_guesses).isnumeric:
                print ("You must have at least 1 guess.")

    print('''I am thinking of a 3-digit number. Try to guess what it is.\nHere are some clues:\nWhen I say:\tThat means:
 Pico\t\tOne digit is correct but in the wrong position.\n Fermi\t\tOne digit is correct and in the right position\n Bagels\t\tNo digit is correct.''')
    
    # digits = int(digits)
    # max_guesses = int(max_guesses)

    ##Stores the secret number
    secret_num = getNum(digits)
    print(secret_num)

    print("I have thought of a number.\nYou have 10 tries to guess the number.")

    guess_num = 1

    while guess_num <= max_guesses:
        guess = ""
        ##Checks to see if the guess is valid
        while len(guess) != digits or not guess.isnumeric():
            print("Guess", guess_num)
            guess = input("> ")
            if len(guess) != digits or not guess.isnumeric():
                print("Your guess must contain only numbers and be {} digits long.".format(digits))

        ##Gives a clue based on the incorrect guess and incremenets the guess number
        if guess != secret_num:       
            getClue(guess, secret_num, digits)
            guess_num += 1
        
        ##Ends the game because the secret number was guessed and prompts the user to play again
        else:
            print("You got it!\nDo you want to play again? (Y / N)")
            new_round = input("> ")
            if new_round == "Y":
                main()
            else:
                exit()

    ##Ends the game because the user had ran out of guesses and prompts them to play again
    print("You lost!\nDo you want to play again? (Y / N)")
    new_round = input("> ")
    if new_round == "Y":
        main()
    else:
        exit()
            

main()
