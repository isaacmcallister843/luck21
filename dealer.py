from deck import Deck 
class Dealer(): 
    def __init__(self) -> None:
        self.hand = []
        self.holeCard = None
        self.score = 0
    
    def dealFirstHand(self, deck: Deck):  # Changed 'Deck' to 'deck'
        self.hand.append(deck.deal())
        self.holeCard = deck.deal()
        self.updateScore()

    
    def updateScore(self): 
        score = 0
        
        score = sum(card.value for card in self.hand)
        score = score +  self.holeCard.value 

        # Check if larger then 21 
        if score > 21:  
            for card in self.hand:
                if card.rank == 'A' and card.value == 11:
                    card.value = 1
                    score = score - 10 
                    # If the score is under 21 after adjustment, break out of the loop
                    print("new score", score)
                    if  score <= 21:
                        break
            if self.holeCard.rank == 'A' and self.holeCard.value == 11: 
                self.holeCard.value = 1 
                score = score - 10
                print("new score", score)

        self.score = score 

    def dealSecondHand(self, deck: Deck):  # Same change here
        while self.score < 17:
            self.hand.append(deck.deal())
            self.updateScore()

    
    def printHand(self): 
        for card in self.hand:
            print(card)
    
    def reset(self): 
        self.hand = []
        self.holeCard = None
        self.score = 0

    
    
