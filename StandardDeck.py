from Card import Card

class StandardDeck:
    deck = []
    
    card_Suit_List = ('Clubs','Diamonds',"Hearts","Spades")
    
    for i in range(4):
        card_Suit = card_Suit_List[i]
        
        for j in range(13):
            card = Card(card_Suit,j)
            deck.append(card)
        
    def pull(self):
        return self.deck.pop(0) 


    def shuffle(self):
        print("To be worked on")