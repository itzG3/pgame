import random
import time
MAX_BET = 20
MIN_BET = 1

def blackjack_greeting():
    print("Welcome to blackjack you already know the rules (;")

def c_credits():
    print("The minium number of credits you can add is $1 and the maximum is $200")
   
    while True:
         
        creds = input("Please enter the amount of credits you'd like to add $")
    
        if creds.isdigit():
            creds = int(creds)
            if 1 <= creds <= 200:
                print(f"Now have loaded ${creds} in credits")
                return creds
            else:
                print("\nPlease enter an ammount within $1-$200")
            
        else:
            print("Please enter a number value between 1 and 200")

def bet_ammount(credits):
    while True:
         
        bet = input(f"Please enter your bet value the minium bet is {MIN_BET} and the max bet is {MAX_BET} $")
    
        if bet.isdigit():
            bet = int(bet)
            if 1 <= bet <= 20 and bet <= credits:
                print(f"You have now bet ${bet}")
                credits -= bet
                print(f"You have ${credits} credits remaining") 
                return credits, bet
            elif bet > credits and MIN_BET <= bet <= MAX_BET:
                print(f"You don't have enough credits you have {credits} remaining ") 
            else:
                print("\nPlease enter an ammount within $1-$20 ")
            
        else:
            print("Please enter a number value between $1 and $20 ")
   
def create_deck():
    suits = ["Diamonds", "Spades", "Hearts", "Clubs"]
    ranks = ["2","3","4","5","6","7","8","9","10", "Jack" , "Queen", "King", "Ace" ]
    deck = []

    for rank in ranks:
        for suit in suits:
    
            if rank in [ "Jack" , "Queen" , "King"] :
                value = 10
            elif rank == "Ace":
                value = 11
            else:
                value = int(rank)
            
            card = {"rank": rank, "suit" : suit, "value" : value }
            deck.append(card)
    
    random.shuffle(deck)
    return deck

def deal_card(deck):
    #deck = create_deck()

    while deck:
        card = deck.pop()
        #print(f"Your card is {card}")
        return card
        

def blackjack():
    while True:
        play_again = input("Are you ready to play? (y/n)").lower()
        
        if play_again == "y":
            time.sleep(1.2)
            #bet_ammount(credits)
            deck = create_deck()

            dealer_cards = []
            player_cards = []
            d_total = 0
            p_total = 0

            #####

            

            player_cards.append(deal_card(deck))
            player_cards.append(deal_card(deck))

            #print(f"Your face up card is {player_cards[0]}")
            #print(f" You were delt: {player_cards[[0]["rank"]]} of {player_cards[[0]["suit"]]} {player_cards[[0]["value"]]} ")
            
            dealer_cards.append(deal_card(deck))
            dealer_cards.append(deal_card(deck))
            print(f"Dealers face up card is {dealer_cards[0]}")

            d_total = sum(card["value"] for card in dealer_cards)
            p_total = sum(card["value"] for card in player_cards)
            
            #for i, card in enumerate(player_cards):
             #   print(f"Your {i+1} card is {player_cards[i]}")
            
            while True:
                if p_total >= 21 and d_total >= 17:
                    print("You win ", p_total , d_total)
                    
                print(f"\nYour cards are {player_cards}")
                print("Your cards total is:" , p_total)

                hit_stand = input("Would you like to hit or stand : ").lower()
                
                if hit_stand == "hit":
                    new_card = deal_card(deck)
                    player_cards.append(new_card)

                    #####
                    used_ace = False
                    for cards in player_cards:
                        if cards["rank"] == "Ace":
                            used_ace = True

                        
                        if p_total > 21 and used_ace :
                            p_total -= 10
                            print("ran p total is", p_total)
                    if used_ace:
                        for cards in player_cards:
                            if cards["rank"] == "Ace":
                                cards["value"] = 1
                                print("ran")
                    
                    

                    #####
                    p_total = sum(card["value"] for card in player_cards)
                    #p_total += new_card["value"]
                    print(f"You pulled {new_card} \n  Your total is {p_total}")
                    time.sleep(1.1)
                    #print(f"Your cards are {player_cards}")
                    if p_total > 21:
                        print("Bust you lose")
                        break


                elif hit_stand == "stand":
                    print(f"Dealers card are {dealer_cards} \nDealers Total is: {d_total}")
                    time.sleep(1.5)
                    while d_total < 17:
                        print(f"Dealers card are {dealer_cards} \nDealers Total is: {d_total}")

                        new_card = deal_card(deck)
                        dealer_cards.append(new_card)
                        
                        d_total += new_card["value"]
                        print(f"Dealer Pulled a {new_card}\nDealers Total is: {d_total}")
                        time.sleep(1.5)
                        if d_total > 21:
                            print("Dealer busts you win!")
                            break
                    
                    
                    if p_total > d_total or d_total > 21:
                        print("You win!") 
                        break
                    elif p_total == d_total:
                        print("Draw")
                        break
                    else:
                        print(f"You lose! \n dealer had {d_total} to your {p_total}")
                        break
                
                elif p_total == 21:
                    while d_total < 17:
                        print(f"Dealers card are {dealer_cards} \n")

                        new_card = deal_card(deck)
                        dealer_cards.append(new_card)
                        
                        d_total += new_card["value"]
                        print(f"Dealer Pulled a {new_card}")
                        if d_total > 21:
                            print("Dealer busts you win!")
                            break
                else:
                    print("Please enter (hit) or (stand)")



        elif play_again =="n":
            c_credits = credits + bet
            print(f'Your bet of ${bet} has been returned')
            break
        else:
            print("Please only enter (Y/N) ")
        

        


if __name__ == "__main__":  
    blackjack_greeting()  
    credits = c_credits()     
    credits, bet = bet_ammount(credits)
    blackjack()
    
