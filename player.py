from deck import Deck 

class Player():
    def __init__(self, startingChips) -> None:
        self.hand = []
        self.score = 0
        self.chips  = startingChips 
        self.currentBet = 0 
    
    def bet(self, amount): 
        if (amount > self.chips): 
            return 0
        self.currentBet = amount 
        return 1 


    def hit(self, deck: Deck): 
        self.hand.append(deck.deal())
        self.updateScore()
    
    def stand(self): 
        return 0 

    def doubleDown(self, deck: Deck): 
        if self.currentBet * 2 > self.chips:
            return 0 
        self.currentBet = self.currentBet * 2
        self.hit(deck)
        return 1 
    
    def surrender(self): 
        self.currentBet = round(self.currentBet/2)
        return 1
    
    def lose(self):
        self.chips = self.chips - self.currentBet
        self.reset()
    
    def reset(self): 
        self.hand = []
        self.score = 0
        self.currentBet = 0 
    

    def updateScore(self): 
        score = 0
        score = sum(card.value for card in self.hand)

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
    
        self.score = score 