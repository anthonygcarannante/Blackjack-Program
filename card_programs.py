import random

# def bet_size():
#     bet = int(input("How much would you like to bet? "))
#     return bet

# Deal the cards & Display the cards
def dealing_cards(deck, pcards, dcards):
    # Dealer's Cards
    while len(dcards) != 2:
        dcards.append(random.choice(deck))
        if len(dcards) == 2:
            print(f"Dealer: X, {dcards[1]}")

    # Player's Cards
    while len(pcards) != 2:
        pcards.append(random.choice(deck))
        if len(pcards) == 2:
            print(f"You:    {pcards[0]}, {pcards[1]}")
    
    return dcards, pcards;

# Sum of the Player Cards
def player_action(deck, pcards, dcards):
    while sum(pcards) <= 21:
        if sum(pcards) == 21:
            print(f"You:    {str(sum(pcards))}, {pcards} ")
            print(f"Dealer: {str(sum(dcards))}, {dcards} ")
            break
        else:    
            action_taken = str(input("Do you want to hit, double, or stay?  "))
            if action_taken == "hit":
                pcards.append(random.choice(deck))
                # if player has at least 11 and hits an ace, then the ace counts as 1
                if pcards[-1] == 11 and sum(pcards) > 10:
                    pcards[-1] -= 10
                print(f"You:    {str(sum(pcards))}, {pcards} ")
            elif action_taken == "double" and len(pcards) == 2:
                pcards.append(random.choice(deck))
                # if player has at least 11 and hits an ace, then the ace counts as 1
                if pcards[-1] == 11 and sum(pcards) > 10:
                    pcards[-1] -= 10
                print(f"You:    {str(sum(pcards))}, {pcards} ")
                break
            elif action_taken == "stay":
                print(f"You:    {str(sum(pcards))}, {pcards} ")
                print(f"Dealer: {str(sum(dcards))}, {dcards} ")
                break
            else:
                print("Incorrect action. Try hit, stay, or double.")
    
    return pcards, dcards;


# Sum of the Dealer Cards
def dealer_action(deck, pcards, dcards):
    while sum(dcards) <= 16 and sum(pcards) <= 21:
        print(f"Dealer HITS")
        dcards.append(random.choice(deck))
        # if the dealer has at least 11 and hits an ace, then the ace counts as 1
        if dcards[-1] == 11 and sum(dcards) > 10:
            dcards[-1] -= 10
        print(f"Dealer: {str(sum(dcards))}, {dcards} ")
        
    return pcards, dcards