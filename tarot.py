# A tarot console reader by Kevin Dibble
# contact: kevin@kevindibble.com

import random

class MajorArcana():

    def __init__(self,number,name,description):
        self.name = name
        self.description = description
        self.number = number

class MinorArcana():
    
    def __init__(self,number,suit):
        self.number = number
        self.suit = suit

class Spread():
    
    def __init__(self,name,number_of_cards):
        self.name = name
        self.number_of_cards = number_of_cards

#Create the Deck
deck = []
suits = ['Wands','Cups','Pentacles','Swords']
m_cards = [["0","The Fool"],["I","The Magician"],["II","The High Priestess"],["III","The Empress"],["IV","The Emperor"],["V","The Hierophant"],["VI","The Lovers"],["VII","The Chariot"],["VIII","Strength"]]

#Itterate through and programatically generate Minor Arcana
for suit in suits:
    for i in range(1,15):
        if i == 1:
            deck.append(MinorArcana("Ace",suit))
        elif i == 2 or i <= 10:
            deck.append(MinorArcana(i,suit))
        elif i == 11:
            deck.append(MinorArcana("Page",suit))
        elif i == 12:
            deck.append(MinorArcana("Knight",suit))
        elif i == 13:
            deck.append(MinorArcana("Queen",suit))
        elif i == 14:
            deck.append(MinorArcana("King",suit))
        i += 1
