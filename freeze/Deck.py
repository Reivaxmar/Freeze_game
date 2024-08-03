import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        # To unicode card conversion
        rnk = self.rank
        if rnk == 12:
            rnk+=1
        elif rnk == -1:
            rnk = 14
        
        a = 0
        if self.suit == "spade":
            a = int("1F0A0", 16) + rnk
        elif self.suit == "heart":
            a = int("1F0B0", 16) + rnk
        elif self.suit == "diamond":
            a = int("1F0C0", 16) + rnk
        elif self.suit == "club":
            a = int("1F0D0", 16) + rnk
        return chr(a)

class Deck:
    SUITS = ["heart", "diamond", "club", "spade"]

    def __init__(self):
        self.cards = []
        self.discards = []
        for rank in range(1, 13):
            for suit in Deck.SUITS:
                self.cards.append(Card(rank, suit))
        
        for suit in Deck.SUITS:
            self.cards.append(Card(-1, suit))

        random.shuffle(self.cards)
    
    def getCard(self) -> Card:
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            raise IndexError("No cards left in the deck")
    
    def discardCard(self, card: Card):
        self.discards.append(card)

    def getTopDiscard(self, discard: bool = False) -> Card:
        # print(f"Len of discards: {len(self.discards)}")
        if len(self.discards) <= 0:
            return 69 # Error
        if discard:
            return self.discards.pop()
        return self.discards[-1]
