

class BetError(Exception):
    def __str__(self):
        return "Bet Error"


class AmountError(Exception):
    def __str__(self):
        return "Amount Error"

class PlayerError(Exception):
    def __str__(self):
        return "Player Error"



