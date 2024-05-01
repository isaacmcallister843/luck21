from dealer import Dealer
from deck import Deck 
from player import Player

class GameManager():
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.hasPlayerLost = False

    def startGameTerminal(self):
        while self.player.chips > 0:
            print(f"Your Chips: {self.player.chips}")
            self.dealer.reset()
            self.player.reset()
            if self.playRoundInTerminal():
                self.player.chips += self.player.currentBet
            else:
                self.player.chips -= self.player.currentBet

    def playRoundInTerminal(self):
        """
        Create a new deck
        """
        newDeck = Deck()

        """
        Check if we have a valid bet, cant bet more then we have
        """
        validBet = False
        while not validBet:
            validBet = self.placeInitialBet()

        """
        Deal out the first hand, check if the dealer won
        """
        self.dealer.dealFirstHand(newDeck)
        if self.checkDealerBlackjack():
            return False 

        """
        Deal out the players hand
        """
        self.player.hit(deck=newDeck)
        self.player.hit(deck=newDeck)
        print(f"Dealer's Hand: {self.dealer.hand[0].name}  :  {self.dealer.score}")
        print(f"Your Hand: {' '.join(str(card) for card in self.player.hand)}  :  {self.player.score}")

        """
        Check if the players score is 21, then they win
        """
        if self.player.score == 21:
            return True
        
        """
        Run the players turn, this is where the player can choose various different actions 
        """
        runGame = True
        while runGame:
            action = input("You can either hit, stand, double down, or surrender: ").lower()
            if not self.playerInput(action=action,deck=newDeck):
                runGame = False
            print(f"Your Hand: {' '.join(str(card) for card in self.player.hand)}  :  {self.player.score}")

            # If the player went over 21 they lose
            if self.player.score > 21:
                return False
            
            # if the player is at exactly 21 they win 
            if self.player.score == 21:
                return True 


        """
        Deal out the second hand for the dealer, they keep going until > 17 
        """
        self.dealer.dealSecondHand(deck=newDeck)
        print(f"Dealer's Hand: {' '.join(str(card) for card in self.dealer.hand)}  :  {self.dealer.score}")


        """
        Final checks, first check if the dealer went over 21
        """
        if self.dealer.score > 21:
            print("You won")
            return True
        
        """
        Compare the scores, if the dealer has a higher score then they win, if you have a higher score you win 
        """

        if self.dealer.score > self.player.score:
            print("Dealer won")
            return False
        else:
            print("Player won")
            return True

    def placeInitialBet(self):
        try:
            initialBet = int(input("Please enter your initial bet: "))
            return self.player.bet(initialBet)  # Assume this returns True if the bet is accepted
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return False

    def playerInput(self, action: str, deck: Deck):
        match action:
            case "hit":
                self.player.hit(deck=deck)
                return True
            case "stand":
                return False
            case "double down":
                if not self.player.doubleDown(deck):
                    print("Not enough chips to double down")
                    return True
                print(f"New Bet: {self.player.currentBet}")
                return False
            case "surrender":
                self.player.surrender()
                self.hasPlayerLost = True
                return False

    def checkDealerBlackjack(self):
        if self.dealer.score == 21:
            print("Dealer's hand is 21, you lost.")
            return True
        return False

newGame = GameManager()
newGame.startGameTerminal()