# Freeze game
The freeze game is a card game that is played with the poker deck. This is the engine for a potential AI implementation. The game is player without jokers.

## How to play
### Beggining of the game
Freeze is a card game that can be played with as many as needed players (but with multiple decks at once). At the beggining of the game, each player is given 4 cards that they cannot look at. They arrange them in a square form (see later how). Before the game starts, every player can look at their two bottom cards once.
### Round logic
Once everyone has seen their two cards, the game starts. A players starts and gets a card either from the top of the deck or from discard pile. That card can only be seen by him (unless he gets it from the discard pile, because everyone has already seen it), and the player can decide either to change it from a card that he has or discard the card. If the card has been taken from the discard pile, that card can't be discarded.
### Winning objective
The winner is decided by the player who has the lower sum of cards. To end the round, you must say "freeze" at the beginning of your turn, and there will be one last round until its your turn once again, where you don't play and the game finishes
### Special cards
There are three special cards: the jack, the queen and the king. If a jack is discarded, the player who discarded the jack can change any two cards from the table, either if they are his or not (or both). When a queen is discarded the player who discarded the queen has the right to look at one card, either one of his or from another player. The jack has a value of 11, the queen a value of 12 and the king a value of -1. The ace has a value of 1.
### Get extra or less cards
There are a few ways one can end up with more or less than 4 cards. When a player discards a card, another player just after can discard a card of the same rank and end up with one less. If the player discards an incorrect card, he keeps the card that has discarded and has to pick up another one. If a player cheats in any way, he will get another card. When you get a card for discarding a wrong card or cheating, you cannot look at the card.

## Installation
It's just a python module, so it can be installed with:
```bash
python3 install -e .
```
And to run it just execute:
```bash
freeze
```