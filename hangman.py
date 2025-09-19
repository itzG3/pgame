### Build a hangman game 

import random



def greethangman():
    print("\n Welcome to Hangman! \nRules to the game: \n Enter only a single letter  \n If you guess the word wrong 5 times you lose! \n Don't worry if you guess it correctly you'll not lose any lives")


def hangman():
    words = [
        "apple", "banana", "grape", "orange", "cherry", "mango", "peach", "lemon", "melon", "kiwi",
              "zebra", "tiger", "panda", "lion", "giraffe", "monkey", "elephant", "rabbit", "kangaroo", "otter",
        "table", "chair", "pillow", "blanket", "window", "mirror", "curtain", "bottle", "basket", "closet",
        "python", "coding", "function", "variable", "integer", "boolean", "compile", "string", "syntax", "loop",
        "rocket", "planet", "galaxy", "astronaut", "satellite", "meteor", "spaceship", "telescope", "gravity", "universe" , "lewis"
    ]

    rword = random.choice(words)

    answer = [x for x in rword]
    
    display_word = ["_" for x in answer]
    guessed_letters = []
    print(display_word)
    
    print(f"The length of the word is {len(answer)} letters")

    counter = 0
    while True:
    
        guess = input("Guess a character: ").lower()
        
        #print(answer)

        if guess in answer:
            print("Good Guess!") 
            for x in range(len(answer)):
                if answer[x] == guess:
                    display_word[x] = guess
            if display_word == answer:
                    print("You nailed it!\nYou win!")
                    break
        elif guess in guessed_letters:
            print("You've already guessed this letter")
            continue  
        elif guess not in answer:
            print("Sorry this character isn't in the word")
            guessed_letters.append(guess)
            print(f"Your guessed letter(s) are {guessed_letters}")
            counter += 1
            print(f"You have {5-counter} incorrect guesses remaining")
        else:
            continue

        if counter == 5:
            print("You lose!!")
            break

        print(f"This is the current word {display_word}")



if __name__ == "__main__":
    greethangman()
    hangman()
    