from . import Deck

class Player:
    def __init__(self, deck, playerNum):
        self.plNum = playerNum
        self.cards = []
        self.started = False
        for i in range(4):
            self.cards.append(deck.getCard())
            # print(self.cards[-1])
    
    def startRound(self):
        # Don't call this twice
        if self.started == True:
            return ":("
        self.started = True
        # Return the two visible cards
        return f"{self.cards[2]}, {self.cards[3]}"
    
    def doTurn(self, deck: Deck.Deck, frozen: bool) -> bool:
        f = False
        if not frozen:
            f = str(input(f"Player {self.plNum}, do you want to freeze? (y/n) "))
            f = (f == "y")
        
        p = False
        if len(deck.discards) > 0:
            p = str(input(f"Player {self.plNum}, do you want to get a card from the discard pile? (y/n) "))
            p = (p == "y")

        card = -1
        if p:
            card = deck.getTopDiscard(True)
        else:
            card = deck.getCard()
        idx = int(input(f"Player {self.plNum}, you got the card {card}, what card do you want to change? (-1 for discard) "))
        if idx == -1:
            deck.discardCard(card)
            print(f"Player {self.plNum}, you have discarded that card {card}")
        else:
            dis = self.cards[idx]
            self.cards[idx] = card
            deck.discardCard(dis)
            print(f"Player {self.plNum}, you have discarded that card {dis}")
        return f

    def checkDiscards(self, lastDiscard: Deck.Card, deck: Deck.Deck):
        numDis = int(input(f"Player {self.plNum}, how many do you want to discard? "))
        for i in range(numDis):
            c = int(input(f"Player {self.plNum}, what card do you want to discard? "))
            self.__tryDiscard(c, deck, lastDiscard)

    def __tryDiscard(self, cardidx, deck: Deck.Deck, lastDiscard: Deck.Card):
        print(f"Tried to discard card {self.cards[cardidx]}")
        if self.cards[cardidx].rank != lastDiscard.rank:
            self.cards.append(deck.getCard())
            print(f"The card {self.cards[cardidx]} hasn't the same rank as {lastDiscard.rank}!")
        else:
            deck.discardCard(self.cards[cardidx])
            print(f"Succesfully discarded the card {self.cards.pop(cardidx)}!")

    def showCards(self):
        print(f"Player {self.plNum} has the cards: ")
        s = 0
        for card in self.cards:
            print(f"- {card}")
            s += card.rank
        return s