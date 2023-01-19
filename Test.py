from StandardDeck import StandardDeck

deck = StandardDeck()

for i in range(55):
    print(deck.pullFromTop())

# does not work right
# deck.shuffle()
