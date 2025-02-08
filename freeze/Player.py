from . import Deck
from . import MessageManager as Mss

class Player:
    def __init__(self, deck, playerNum):
        self.mss = Mss.MessageManager()
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
    
    def doTurn(self, deck: Deck.Deck, frozen: bool):
        f = False
        if not frozen:
            f = str(self.mss.privateAsk("do you want to freeze? (y/n)", self.plNum))
            f = (f == "y")
        
        p = False
        if len(deck.discards) > 0:
            p = str(self.mss.privateAsk("do you want to get a card from the discard pile? (y/n)", self.plNum))
            p = (p == "y")

        card = -1
        if p:
            card = deck.getTopDiscard(True)
        else:
            card = deck.getCard()
        idx = int(self.mss.privateAsk(f"you got the card {card}, what card do you want to change? (-1 for discard)", self.plNum))
        discard = 0
        if idx == -1:
            deck.discardCard(card)
            self.mss.publicPrint(f"Player {self.plNum} has discarded the card {card}")
            discard = card
        else:
            dis = self.cards[idx]
            self.cards[idx] = card
            deck.discardCard(dis)
            self.mss.publicPrint(f"Player {self.plNum} has discarded the card {dis}")
            discard = dis
        return f, discard

    def checkDiscards(self, lastDiscard: Deck.Card, deck: Deck.Deck):
        wantDis = self.mss.privateAsk("do you want to discard any cards? (y/n)", self.plNum)
        if(wantDis == "y"):
            while(True):
                c = int(self.mss.privateAsk("what card do you want to discard? (-1 to cancel)", self.plNum))
                if c == -1: break
                self.__tryDiscard(c, deck, lastDiscard)
            

    def __tryDiscard(self, cardidx, deck: Deck.Deck, lastDiscard: Deck.Card):
        self.mss.publicPrint(f"Player {self.plNum} has tried to discard card {self.cards[cardidx]}")
        if self.cards[cardidx].rank != lastDiscard.rank:
            self.cards.append(deck.getCard())
            self.mss.publicPrint(f"The card {self.cards[cardidx]} hasn't the same rank as {lastDiscard.rank}!")
        else:
            deck.discardCard(self.cards[cardidx])
            self.mss.publicPrint(f"Succesfully discarded the card {self.cards.pop(cardidx)}")

    def showCards(self):
        self.mss.publicPrint(f"Player {self.plNum} has the cards: ")
        s = 0
        for card in self.cards:
            self.mss.publicPrint(f"- {card}")
            s += card.rank
        return s
    
    def askShow(self):
        pl = int(self.mss.privateAsk(f"what player do you want to see the card from?", self.plNum))
        card = int(self.mss.privateAsk(f"what card do you want to pick?", self.plNum))
        return pl, card
    
    def tellShow(self, card: Deck.Card):
        self.mss.privatePrint(f"The player has the card {card}", self.plNum)

    def getCard(self, idx):
        return self.cards[idx]