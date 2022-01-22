import random, csv

### BlackJack Game ###

# Dealer Cards
dealer_cards = []

# Player Cards
player_cards = []

print("-----------------------------------")

# Deal the cards & Display the cards
# Dealer's Cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print(f"Dealer: X, {dealer_cards[1]}")

# Player's Cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print(f"You:    {player_cards[0]}, {player_cards[1]}")

# Sum of the Player Cards
while sum(player_cards) <= 21:
    if sum(player_cards) == 21:
        break
    else:    
        action_taken = str(input("Do you want to hit, double, or stay?  "))
        if action_taken == "hit":
            player_cards.append(random.randint(1,11))
            # if player has at least 11 and hits an ace, then the ace counts as 1
            if player_cards[-1] == 11 and sum(player_cards) > 10:
                player_cards[-1] -= 10
            print(f"You:    {str(sum(player_cards))}, {player_cards} ")
        elif action_taken == "double" and len(player_cards) == 2:
            player_cards.append(random.randint(1,11))
            # if player has at least 11 and hits an ace, then the ace counts as 1
            if player_cards[-1] == 11 and sum(player_cards) > 10:
                player_cards[-1] -= 10
            print(f"You:    {str(sum(player_cards))}, {player_cards} ")
            break
        elif action_taken == "stay":
            print(f"You:    {str(sum(player_cards))}, {player_cards} ")
            print(f"Dealer: {str(sum(dealer_cards))}, {dealer_cards} ")
            break
        else:
            print("Incorrect action. Try hit, stay, or double.")

# Sum of the Dealer Cards
while sum(dealer_cards) <= 16 and sum(player_cards) <= 21:
    print(f"Dealer HITS")
    dealer_cards.append(random.randint(1,11))
    # if the dealer has at least 11 and hits an ace, then the ace counts as 1
    if dealer_cards[-1] == 11 and sum(dealer_cards) > 10:
        dealer_cards[-1] -= 10
    print(f"Dealer: {str(sum(dealer_cards))}, {dealer_cards} ")

# Player and Dealer Hand Comparisons 
if sum(player_cards) == 21 and len(player_cards) == 2:
    print(f"BLACKJACK! You WIN!")
elif sum(player_cards) > 21:
    print(f"Dealer: {str(sum(dealer_cards))}, {dealer_cards} ")
    print("You BUSTED!")
    print("Dealer WINS!")
elif sum(player_cards) <= 21 and sum(dealer_cards) > 21:
    print("Dealer BUSTED!")
    print("You WIN!")
elif sum(player_cards) <= 21 and sum(dealer_cards) <= 21:
    if sum(player_cards) > sum(dealer_cards):
        print(f"You WIN!")
    elif sum(player_cards) < sum(dealer_cards):
        print(f"Dealer WINS!")
    else:
        print(f"PUSH")
else:
    print("Nothing Happened")

print("-----------------------------------")

# Store results in CSV file for analysis


# Compare the sums of the dealer and player cards
# If P sum is greater than 21 = BUST
# If P sum is less than 21 = Option (Hit or Stay)
# If P option Stay, compare sum of D and P
# If P sum < 21 AND > D sum, then P wins
# If P sum < 21 And < D sum, then P loses