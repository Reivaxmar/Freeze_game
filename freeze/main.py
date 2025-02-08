from . import Deck, Player

def main():
    deck = Deck.Deck()
    players = []
    NUM_PLAYERS = 2
    for i in range(NUM_PLAYERS):
        players.append(Player.Player(deck, i))
    
    # Look round
    for i in range(NUM_PLAYERS):
        print(f"Player {i} bottom cards are: {players[i].startRound()}")

    frozen = False
    whoFroze = -1
    curTurn = 0
    while True:
        # Check for game finish
        if frozen and whoFroze == curTurn:
            break
        # Do the turn of the current player
        frozen_val, info = players[curTurn].doTurn(deck, frozen)
        frozen = max(frozen_val, frozen)
        if frozen and whoFroze == -1:
            whoFroze = curTurn
        # Check for Q (show card)
        if info.rank == 12:
            pl, idx = players[curTurn].askShow()
            players[curTurn].tellShow(players[pl].getCard(idx))
        # Check for J (swap cards)
        if info.rank == 11:
            exit(-1)
        # Make all the players check for discards on that last discarded
        for player in players:
            player.checkDiscards(deck.getTopDiscard(), deck)
        # Next turn
        curTurn += 1
        curTurn %= NUM_PLAYERS
    
    winners = []
    curBest = 999999
    for player in players:
        s = player.showCards()
        if s < curBest:
            winners.clear()
        if s <= curBest:
            curBest = s
            winners.append(player.plNum)
    
    if len(winners) == 1:
        print(f"The winner is Player {winners[0]} with {curBest} points!")
    else:
        print(f"There are {len(winners)} winners in this game! They are:")
        for winner in winners:
            print(f"- Player {winner} with {curBest} points")


if __name__ == "__main__":
    main()
