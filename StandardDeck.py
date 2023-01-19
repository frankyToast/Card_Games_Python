from Card import Card
import random

class StandardDeck:
    deck = []
    
    card_Suit_List = ('Clubs','Diamonds',"Hearts","Spades")
    
    for i in range(4):
        card_Suit = card_Suit_List[i]
        
        for j in range(1,14):
            card = Card(card_Suit,j)
            deck.append(card)
        
    def pullFromTop(self):
        if len(self.deck) > 0:
            return self.deck.pop(0) 

    # def shuffle(self):
    #     for i in range(52):
    #         temp = self.deck[i]
    #         self.deck[i]= self.deck[random.randint(1,13)]