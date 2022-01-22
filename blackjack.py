import csv
import pandas as pd
from card_programs import dealing_cards, dealer_action, player_action

### BlackJack Game ###

# Define card options so they match the probabilities in a deck of cards. There are four "tens" in the deck for blackjack
cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]

play = "yes"
money = 500
hand_list = []
bankroll = []
player_stats = {"Hand": [], "Cards": []}
dealer_stats = {"Hand": [], "Cards": []}

while play == "yes" and money > 0:
    print("-----------------------------------")
    print(f"Bankroll: ${money}")
    # Track amount of money before the hand started
   
    # Dealer Cards
    dealer_cards = []

    # Player Cards
    player_cards = []

    # Bet before cards are dealt
    bet = int(input("How much would you like to bet? "))

    # Deal the cards
    dealing_cards(cards, player_cards, dealer_cards)

    # Player acts
    player_action(cards, player_cards, dealer_cards)

    # Dealer acts
    dealer_action(cards, player_cards, dealer_cards)

    # Player and Dealer Hand Comparisons 
    # If the player hits blackjack (i.e., 21 on their first two cards)
    if sum(player_cards) == 21 and len(player_cards) == 2:
        print(f"BLACKJACK! You WIN!")
        money += bet * 3/2
    # If the player busts, or gets a hand over 21
    elif sum(player_cards) > 21:
        print(f"Dealer: {str(sum(dealer_cards))}, {dealer_cards} ")
        print("You BUSTED!")
        print("Dealer WINS!")
        money -= bet
    # If the player is under 21 and the dealer busts
    elif sum(player_cards) <= 21 and sum(dealer_cards) > 21:
        print("Dealer BUSTED!")
        print("You WIN!")
        money += bet
    # If neither the player nor the dealer bust
    elif sum(player_cards) <= 21 and sum(dealer_cards) <= 21:
        # If the player's hand is higher, player wins
        if sum(player_cards) > sum(dealer_cards):
            print(f"You WIN!")
            money += bet
        # If the dealer's hand is higher, dealer wins
        elif sum(player_cards) < sum(dealer_cards):
            print(f"Dealer WINS!")
            money -= bet
        # If the player and dealers hands are the same
        else:
            print(f"PUSH")
    else:
        print("Nothing Happened")

    print("-----------------------------------")

    # Compile stats
    player_stats["Hand"].append(sum(player_cards))
    player_stats["Cards"].append(player_cards)
    dealer_stats["Hand"].append(sum(dealer_cards))
    dealer_stats["Cards"].append(dealer_cards)
    bankroll.append(money)

    play = str(input("Would you like to deal another hand? (yes/no)  "))

print("-----------------------------------")
print(f"New Balance: ${money}")
print("-----------------------------------")

data = [[player_stats["Hand"],player_stats["Cards"],dealer_stats["Hand"],dealer_stats["Cards"],bankroll]]
blackjack_stats_df = pd.DataFrame(data, columns=['Player Hand','Player Cards','Dealer Hands','Dealer Cards','Bankroll'])

blackjack_stats_df.to_csv('blackjack_data.csv')