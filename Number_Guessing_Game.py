import random

print("------------------------------------")
print("Welcome to the Number Guessing Game!")
print("------------------------------------")


start_game = True
highscore = []

while start_game:
    try:
        guess_number = random.randrange(1, 11)
        number = 0
        number_of_tries = 0
        while number != guess_number:
            
            number = input("Pick a number between 1 and 10: ")
            number = int(number)
            number_of_tries += 1
            
            if number > guess_number:
                print("It is lower!")
            elif number < guess_number:
                print("It is higher!")
            else:
                print("You got it! It took you {} tries".format(number_of_tries))
                break
        
        start_again = input("Would you like to play again? [y]es/[n]o: ")
        if start_again == "y":
            highscore.append(number_of_tries)
            print("The HIGHSCORE is {}".format(min(highscore)))
            continue
        else:
            break
    except ValueError:
        print("This is not a number! Start again")
    
