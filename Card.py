import random

class Card:
    card_type = ""
    card_Num = -1

    def _init_(self, card_Type, card_Num):
        card_Types_List = ('Spades','Hearts', "Clubs","Diamonds")
        self.card_Type = random.choice(card_Types_List)
        self.card_Num = random.randrange()

    def get_Type(self):
        return self.card_Type
    
    def get_Num(self):
        return self.card_Num