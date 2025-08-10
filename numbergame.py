import random
# Game to guess number between 1-100
# Tell user higher or lower
# They have 8 guesses to get the right number

def welcome():
    print("\nWelcome Higher or Lower I hope that you enjoy")
    print("Your Job is to guess the random number between 1 and 100")
    print("You will be told if the number is higher or lower \n")


def higherlower():
    answer = random.randint(1,100)
    nr_guesses = 8 

    for i in range(nr_guesses):

        while True:
            guess = input("Please enter your guess from 1-100: ")
            
        
            try:
                uguess = int(guess)

                if not (1 <= uguess <= 100):
                        print("Please enter a number between 1 and 100")
                else:
                    break
            except:
                    print("Please enter only a number ")
                    

        # Game outputs 

        if uguess == answer:
            print(f"\n You win! \n It only took {i} guesses! \n")
            break
        elif i == 7:
            print("You lose better luck next time! \n")
        elif uguess > answer:
            print(f"Your guess was higher, you have {7-i} guesses remaining \nGuess a little lower (; ")
        elif uguess < answer:
            print(f"Your guess was lower, you have {7-i} guesses remaining \nGuess a little higher (; ")
        else:
            break


if __name__ == "__main__":
    welcome()
    higherlower()