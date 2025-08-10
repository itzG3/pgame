from guessgame import start_game , choice_game
from numbergame import welcome ,  higherlower
from hangman import hangman , greethangman
from blackjack import blackjack_greeting , c_credits , blackjack , bet_ammount
import time



def main_loop():
    while True:

        time.sleep(2)

        print("Welcome to text games!!")
        menu_option = input("Please enter a choice of \n 0 To exit \n 1 to play Code Guesser \n 2 to play Higher or Lower \n 3 to play Hangman \n 4 to play BlackJack \n Enter Choice: ")

        try:
            choice = int(menu_option)

            #print(f"debug : You entered choice:  {choice} \n")

            if choice == 0:
                break
            elif choice == 1:
                #run guessgame

                start_game()
                choice_game()

            elif choice == 2:
                #run numbergame

                welcome()
                higherlower()
            elif choice == 3:
                # run hangman
                greethangman()
                hangman()

            elif choice == 4:
                blackjack_greeting()  
                credits = c_credits()     
                credits, bet = bet_ammount(credits)
                blackjack()

            else:
                print("Please enter a vaild number option 0, 1 , 2")
        except:
            print("\n Please enter a vaild option: 0 , 1 , 2 , 3 \n")

main_loop()