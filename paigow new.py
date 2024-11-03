import random

def create_deck():
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['ace','2', '3', '4', '5', '6' , '7', '8', '9', '10', 'jack', 'queen', 'king']
    deck = [(value, suit) for suit in suits for value in values]
    deck.append('joker')
    random.shuffle(deck)
    return deck

def draw_card(deck):
    if deck:
        return deck.pop()
    else:
        print("the deck is empty, shuffling again...")
        return None

def changecards(playershand,dealershand):
    answer= int(input("Whos turn is it? 1= dealer 2= player:"))
    print("Your current hands:")
    if answer == 1:
        print(f"Low hand: {playershand[:2]}")
        print(f"High hand: {playershand[2:7]}")
    elif answer == 2:
        print(f"Low hand: {playershand[:2]}")
        print(f"High hand: {playershand[2:7]}")
    elif  answer != 1 and answer != 2:
         print("input vaild num 1 or 2")
    else:
        print("invaild input. input vaild num")
            
    print("\n")
    print("The first 2 cards (0-1) will be the low hand and the last 5 cards (2-6) will be the high hand.")
    answer = input("Would you like to switch your cards? (y/n): ").lower()
    if answer == "y":
        pos1 = int(input("Which card would you like to switch (0-6)? "))
        pos2 = int(input("Which card would you like to switch (0-6)? "))
        if answer == 1:
            dealershand[pos1], dealershand[pos2] = dealershand[pos2], dealershand[pos1]
            print("\n")
            print("New hands:")
            print(f"Low hand: {playershand[:2]}")
            print(f"High hand: {playershand[2:7]}")
        elif answer == 2:
            playershand[pos1], playershand[pos2] = playershand[pos2], playershand[pos1]
            print("\n")
            print("New hands:")
            print(f"Low hand: {playershand[:2]}")
            print(f"High hand: {playershand[2:7]}")
    elif answer == "n":
        print("Keeping current hands.")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

def evaluate_hand(hand):
    values_points = {
        'ace': 11,
        '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10, 'jack': 11, 'queen': 12, 'king': 13
    }
    ##maybe dont need this or ask if the want 1 or 11 
    total_points = 0
    for card in hand:
        if card != 'joker':  # Exclude jokers from evaluation
            value, _ = card
            total_points += values_points[value]

    # If total points exceed 21, treat aces as 1 instead of 11 
    num_aces = sum(1 for card in hand if card[0] == 'ace')
    while total_points > 21 and num_aces > 0:
        total_points -= 10
        num_aces -= 1

    return total_points

def main():
    playershand = []
    dealershand = []
    deck = create_deck()

    # Dealer's turn
    for _ in range(2):
        for _ in range(7):
            card = draw_card(deck)
            dealershand.append(card)

    # Player's turn
    for _ in range(2):
        for _ in range(7):
            card = draw_card(deck)         
            playershand.append(card)
    answer = "y"
    while answer == "y":
        changecards(playershand, dealershand)
        answer = input("Would you like to switch  between players? (y/n): ").lower()

    # Split player's hand into low and high hands
    player_lowhand, player_highhand = playershand[:2], playershand[2:7]

    # Split dealer's hand into low and high hands
    dealer_lowhand, dealer_highhand = dealershand[:2], dealershand[2:7]

    # Evaluate hands
    player_lowtotal = evaluate_hand(player_lowhand)
    player_hightotal = evaluate_hand(player_highhand)
    dealer_lowtotal = evaluate_hand(dealer_lowhand)
    dealer_hightotal = evaluate_hand(dealer_highhand)

    print(f"\nPlayer's total: {player_lowtotal}, {player_hightotal}")
    print(f"Dealer's total: {dealer_lowtotal}, {dealer_hightotal} ")

    if player_lowtotal > dealer_lowtotal and player_hightotal > dealer_hightotal:
        print("Player wins!")
    elif player_lowtotal < dealer_lowtotal and player_hightotal < dealer_hightotal:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Play the game
main()
