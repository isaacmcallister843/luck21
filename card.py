class Card(): 
    def __init__(self, suit: str, rank: str) -> None:
        """
        suit: specifies the suit, either C,D,S,H 
        """
        """
        Name: whats on the card, A-9, J,Q,K 
        """
        self.suit = suit 
        self.rank = rank 
        self.value = self.rank_to_value(rank)
        self.name =  f"{suit}{rank}"
    def __str__(self) -> str:
        # This method allows printing the card's name directly
        return self.name


    @staticmethod
    def rank_to_value(rank: str) -> int:
        # Map ranks to their respective values
        rank_values = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
        }
        return rank_values.get(rank, 0)  # Default to 0 if rank is not recognized

    

        