#TODO: simplify algorithm into a turn based game loop
#TODO: get rid of duplication ex: score

import random


print("Welcome to Blackjack")

def deal(length = 1):
    return [random.randint(1, 11) for _ in range(length)]

def print_state(dealers_turn = False):
    print(f"Your hand: {player_hand} = {sum(player_hand)}")
    if not dealers_turn:
        print(f"Dealer's hand: {dealer_hand[0]}")
    else:
        print(f"Dealer's hand: {dealer_hand} = {sum(dealer_hand)}")

def busted():
    if sum(player_hand) > 21:
        print("Bust! You lose.")
        return True
    elif sum(dealer_hand) > 21:
        print("Dealer busts! You win.")
        return True
    else:
        return False
    
def determine_winner():
    print(f"You have {sum(player_hand)}")
    print(f"Dealer has {sum(dealer_hand)}")
    player_score = sum(player_hand)
    dealer_score = sum(dealer_hand)
    if dealer_score >= player_score and dealer_score <= 21:
        print("Dealer wins.")
    elif player_score > dealer_score and player_score <= 21:
        print("You win!")

player_hand = deal(2)
dealer_hand = deal(2)

print_state()

# Player's turn
hit = True
while hit:
    hit =  input("Do you want to hit? Type 'y' for yes or 'n' for no: ").lower() == 'y'
    if hit:
        player_hand += deal()
        print_state()
        if busted():
            hit = False

# Dealer's turn
print_state(True)
def dealer_losing():
    return sum(player_hand) > sum(dealer_hand)

while dealer_losing() and not busted():
    dealer_hand += deal()
    print_state(True)

determine_winner()