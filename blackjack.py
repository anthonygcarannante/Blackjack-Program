import csv
from card_programs import dealing_cards, dealer_action, player_action

### BlackJack Game ###

# Dealer Cards
dealer_cards = []

# Player Cards
player_cards = []

# Define card options so they match the probabilities in a deck of cards. There are four "tens" in the deck for blackjack
cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]

print("-----------------------------------")

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
# If the player busts, or gets a hand over 21
elif sum(player_cards) > 21:
    print(f"Dealer: {str(sum(dealer_cards))}, {dealer_cards} ")
    print("You BUSTED!")
    print("Dealer WINS!")
# If the player is under 21 and the dealer busts
elif sum(player_cards) <= 21 and sum(dealer_cards) > 21:
    print("Dealer BUSTED!")
    print("You WIN!")
# If neither the player nor the dealer bust
elif sum(player_cards) <= 21 and sum(dealer_cards) <= 21:
    # If the player's hand is higher, player wins
    if sum(player_cards) > sum(dealer_cards):
        print(f"You WIN!")
    # If the dealer's hand is higher, dealer wins
    elif sum(player_cards) < sum(dealer_cards):
        print(f"Dealer WINS!")
    # If the player and dealers hands are the same
    else:
        print(f"PUSH")
else:
    print("Nothing Happened")

print("-----------------------------------")

# Store results in CSV file for analysis
