from card import Card 
import random

class Deck():
    def __init__(self) -> None:
        self.currentDeck = self.generateDeck()
    
    @staticmethod
    def generateDeck(): 
        deck = [] 
        suits = ["C","D","S","H"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "K", "Q", "J"]
        for suit in suits: 
            for rank in ranks: 
                deck.append(Card(suit, rank))

        random.shuffle(deck)
        return deck
    
    def printDeck(self): 
        for item in self.currentDeck: 
            print(item.name)
    
    def deal(self): 
        # Deals the first card 
        return self.currentDeck.pop(0)


