#!/usr/local/bin/python3
import random 
'''

In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

    You need to create a simple text-based BlackJack game
    The game needs to have one player versus an automated dealer.
    The player can stand or hit.
    The player must be able to pick their betting amount.
    You need to keep track of the player's total money.
    You need to alert the player of wins, losses, or busts, etc...

And most importantly:

    You must use OOP and classes in some portion of your game. 
    You can not just use functions in your game. Use classes to help you define the Deck and the Player's hand. 
    There are many right ways to do this, so explore it well!

'''

#---------------------------------
#   Global Variables
#---------------------------------
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#---------------------------------
#   Card Class
#---------------------------------
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + ' of ' + self.suit

#---------------------------------
#   Deck Class
#---------------------------------
class Deck:
    def __init__(self):
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank)) 
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()

#---------------------------------
#   Player Class
#---------------------------------
class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = [] 
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def stand_or_hit(self):
        action = input('Would you like to stand or hit (S|H): ').upper
        
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

#---------------------------------
#   Main Functionality
#
#   1. 
#
#---------------------------------

