# A tarot console reader by Kevin Dibble
# contact: kevin@kevindibble.com

import random

class MajorArcana():

    def __init__(self,name,description):
        self.name = name
        self.description = description

class MinorArcana():
    
    def __init__(self,number,suit):
        self.number = number
        self.suit = suit

class Spread():
    
    def __init__(self,name,number_of_cards):
        self.name = name
        self.number_of_cards = number_of_cards