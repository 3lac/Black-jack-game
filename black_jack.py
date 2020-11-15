# DeckOfCards.py Class object in Python that generates a deck of cards in random order
import random
all_values = [ "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "K", "Q", "J"]
all_suits = ["Diamonds", "Clubs", "Hearts", "Spades"]

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.game_value = None

    def show_card(self):
        print(" ____")
        print(f"|{self.value}{self.suit}  |".rjust(4))
        print("|    |")
        print("|    |")
        print(" -----")

    def __str__(self):
        return (f"{self.value},{self.suit}")

class DeckOfCards:
    def __init__(self):
        self.cards = [""] * 52
        i = 0
        while i < 52:
            for values in all_values:
                for suits in all_suits:
                    self.cards[i] = Card(values, suits)
                    i += 1
            random.shuffle(self.cards)

    def __str__(self):
        return str([str(card) for card in self.cards])

    def remove_card(self):
        return self.cards.pop()

def black_jack(Deck_of_cards):
    dealer = []
    player = []
    for card in Deck_of_cards.cards:
        if card.value in ("JKQA"):
            card.game_value = 10
        elif card.value == "A":
            card.game_value =
        else:
            cards.game_value = int(cards.value)
    dealer.append(Deck_of_cards.remove_card())
    player.append(Deck_of_cards.remove_card())
    player.append(Deck_of_cards.remove_card())
    player_total = player[0].game_value + player[1].game_value
    dealer_total = dealer[0].game_value
    print(f"Player has {player[0]} and {player[1]}")
    print(f"Your Total is {player_total}")
    end_of_turn = "continue"
    player_number_of_cards = 2
    dealer_number_of_cards = 1
    while player_total < 21 and end_of_turn == "continue":
        player_move = input("H for hit and S for stand: ")
        if player_move == "H":
            new_card = Deck_of_cards.remove_card()
            player_total += new_card.game_value
            player.append(new_card)
            print(f"Your additonal card is {new_card.value} of {new_card.suit}")
            print(f"Your new total is {player_total}")
            if player_total > 21:
                print("BUSTED")
                end_of_turn = "done"
            if player_total == 21:
                print("You got 21")
                end_of_turn = "done"


def main():
    a = DeckOfCards()
    black_jack(a)

main()

