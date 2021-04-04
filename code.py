import random

# These are the card suit ranks and values

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3 ,'Four': 4,'Five': 5,'Six': 6,'Seven': 7,'Eight': 8,'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


## Card Class this is making a Card that will later be make into a deck 

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        print (f'This card is the {self.value} of {self.suit}')

three_of_clubs = Card('Clubs', 'Three')
two_of_hearts = Card('Hearts', 'Two')

print(three_of_clubs.value)
print(two_of_hearts.value)

print(two_of_hearts.value < three_of_clubs.value)