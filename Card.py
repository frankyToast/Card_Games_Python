import random

class Card:
    def __init__(self,suit,num) -> None:
        self.suit_type = suit
        self.card_Num = num
        
    def get_Suit(self):
        return self.suit_type
    
    def get_Num(self):
        match self.card_Num:
            case 11:
                return 'Jack'
            case 12:
                return 'Queen'
            case 13:
                return 'King'
            case 1:
                return 'Ace'
            case _:
                return self.card_Num

    def __str__(self) -> str:
        return (f'{self.get_Num()} of {self.get_Suit()}')