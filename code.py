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

### Now I am taking my card class and basically making it into a deck that while shuffle when a new instance of the deck is made

class Deck:

    def __init__(self):
        #empyt list where i will put my deck 
        self.all_cards = []
        #creating all 52 cards in a deck
        for suit in suits:
            for rank in ranks:
                #this creates the card object
                create_card = Card(suit,rank)
                self.all_cards.append(create_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

#### Making the Player Class

class Player:

    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_card(self):
        return self.all_cards.pop(0)
    def add_card(self,new_cards):
        #adding a list of multiple cards in a list 
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            #just one card now 
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards'


new_player = Player('Oscar')

print(new_player)