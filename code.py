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

##### setting the game up 
player_one = Player('Oscar')
player_two = Player('Sophia')

new_deck = Deck()
new_deck.shuffle()

for x in range (26):
    player_one.add_card(new_deck.deal_one())
    player_two.add_card(new_deck.deal_one())

game_on = True 
#####game logic 

round_num = 0 

while game_on:
    round_num += 1
    print(f'Number of rounds {round_num}!!')

    #determine a loser 

    if len(player_one.all_cards) == 0:
        print ('Oscar is out of cards! Sophia has Won!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print ('Sophia is out of cards! Oscar has Won!')
        game_on = False
        break

    # Start a round 
    player_one_cards = []
    player_one_cards.append(player_one.remove_card())
    player_two_cards = []
    player_two_cards.append(player_two.remove_card())

    # When players pull out the same card and war is started

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)

            at_war = False

        else:
            print('WAR!!!!!!')

            if len(player_one.all_cards) < 5:
                print('Oscar was unable to declare war!')
                print('Sophia wins')
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print('Sophia was unable to declare war!')
                print('Oscar Two wins')
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())
