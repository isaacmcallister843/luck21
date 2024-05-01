from dealer import Dealer
from deck import Deck 
from player import Player

class GameManager():
    def __init__(self, minInitialBet=20, maxInitialBet=150, initialChips = 200):
        self.player = Player(startingChips=initialChips)
        self.dealer = Dealer()
        self.minInitialBet = minInitialBet
        self.maxInitialBet = maxInitialBet

        self.surrender = False

    def startGameTerminal(self):
        while self.player.chips >= self.minInitialBet:
            print(f"Your Chips: {self.player.chips}")
            self.dealer.reset()
            self.player.reset()

            match(self.playRoundInTerminal()):
                case 0:
                    print(" -------- You lost")
                    self.player.chips -= self.player.currentBet
                case 1: 
                    print(" -------- You won")
                    self.player.chips += self.player.currentBet
                case 2: 
                    print(" -------- Tie, reseting")
            self.surrender = False

    def playRoundInTerminal(self):
        """
        Returns 0 if the dealer wins, 1 if the dealer wins, and 2 if there is a tie  
        """
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
        Deal out the first hand to the dealer 
        """
        self.dealer.dealFirstHand(newDeck)

        """
        Deal out the players hand
        """
        self.player.hit(deck=newDeck)
        self.player.hit(deck=newDeck)
        print(f"Dealer's Visible Hand: {self.dealer.hand[0].name}")
        print(f"Your Hand: {' '.join(str(card) for card in self.player.hand)}  :  {self.player.score}")

        """
        Check if the players score is 21, then they win
        """
        if (self.player.score != 21) and (self.dealer.score == 21) :
            # Dealer wins 
            print(" ---- Dealer has 21")
            return 0
        if (self.player.score == 21) and (self.dealer.score != 21) :
            # Player wins 
            print(" ---- You have 21")
            return 1
        if (self.player.score == 21) and (self.dealer.score == 21) :
            # Tie 
            print(" ---- Both have 21")
            return 2
        
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
                print(" ---- You are over 21")
                return 0
            
            # if the player is at exactly 21 they win 
            if self.player.score == 21:
                print(" ---- You have exactly 21")
                return 1 
        
        """Check if we surrendered"""
        if(self.surrender): return 0

        """
        Deal out the second hand for the dealer, they keep going until > 17 
        """
        self.dealer.dealSecondHand(deck=newDeck)
        print(f"Dealer's Hand: {' '.join(str(card) for card in self.dealer.hand)} " , self.dealer.holeCard, f"  :  {self.dealer.score}")

        """
        Final checks, first check if the dealer went over 21
        """
        if self.dealer.score > 21:
            print(" ---- Dealer score is larger then 21")
            return 1
        
        """
        Compare the scores, if the dealer has a higher score then they win, if you have a higher score you win 
        """
        if(self.dealer.score == self.player.score): 
            print(" ---- You and the dealer have the same score")
            return 2 
        if self.dealer.score > self.player.score:
            print(" ---- Dealer has a larger score then you ")
            return 0
        else:
            print(" ---- You have a larger score then the dealer")
            return 1

    def placeInitialBet(self):
        try:
            initialBet = int(input("Please enter your initial bet: "))
            # Check if bet is inside the bounds 
            if((initialBet > self.maxInitialBet) or (initialBet < self.minInitialBet)):
                print("Not in betting limit")
                return False
            return self.player.bet(initialBet)  # Assume this returns True if the bet is accepted
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return False

    def playerInput(self, action: str, deck: Deck):
        """
        Returns True if the player can take more actions
        Returns False if the player cant take any more actions 
        """
        match action:
            case "hit":
                self.player.hit(deck=deck)
                return True
            case "stand":
                return False
            case "double down":
                if len(self.player.hand) > 2: 
                    print("Can't double down after hitting")
                    return True
                if not self.player.doubleDown(deck):
                    print("Not enough chips to double down")
                    return True
                print(f"New Bet: {self.player.currentBet}")
                return False
            case "surrender":
                self.player.surrender()
                self.surrender = True
                return False

    
newGame = GameManager()
newGame.startGameTerminal()