import random
# Build a game to guess 4 digit code:
# Options are [R,G,B,Y,W,O]
# User gets 10 tries 
# Each time output:
# You have {3} correct tries


def start_game():
    print("\n Welcome to Code Guess V1.0")
    print("How to play: ")
    print("You are given 6 characters [R,G,B,Y,W,O]")
    print("A random 4 digit code is generated made from these characters")
    print("Your job is to guess the 4 digit code made up of these characters")
    print("The Rules are as follows: ")
    print("You can only enter a valid character [R,G,B,Y,W,O]")
    print("You have a maximum of 10 guesses to figure out the code")
    print("You will also be provided with the number of correct characters in your guess to aid you")
    print("Lastly if you would like to exit the game just enter 0")
    print("I wish you the best of luck code cracker!\n")
    

def choice_game():
    options = ["R","G","B","Y","W","O"]
    
    answer = random.choices(options, k = 4)
    #print(f"answer is {answer}")
    for i in range(1,11): 
        print("Please enter four character from [R,G,B,Y,W,O]")

        while True:
            itr = 0
            guess = list(map(str,input(f"You have {11-i} guesses remaining: ").upper()))
            guess = [x for x in guess if x.strip()]
            print(guess)
            
            if guess == ['0']:
                return "Goodbye"
                
            elif len(guess) != 4:
                print("Please enter 4 characters \n")
                
            elif guess != ['0']:
                for char in guess:
                    if char not in "RGBYWO":
                        print(f"\nPlease only enter the characters (R,G,B,Y,W,O) \n ")
                        break
                    else:
                        itr += 1
            if itr == 4:
                break
            
        if guess == answer:
            print(f"\nYou win!\nIt only took you {i} guesses!")
            break
        elif i == 10:
            print(f"You lose the correct PIN was {answer}")
        elif guess == 0:
            break
        else:
            print(f"You have {nr_correct(guess, answer)} correct character(s) \n")

def nr_correct(guess, answer):
    counter = 0
    for i, char in enumerate(answer):
        if char == guess[i]:
            counter += 1
    return counter

if __name__ == "__main__":
    start_game()
    choice_game()