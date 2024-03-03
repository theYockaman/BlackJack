

class Card:
    VALUES = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"jack":10,"queen":10,"king":10,"ace":11}
    SUITS = ["club","spade","diamond","heart"]

    def __init__(self, value:str, suit:str):

        # Setting the Value
        self.value = value

        # Setting the Suit
        self.suit = suit

        # Setting the TrueValue
        self.trueValue = None

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value:str) -> None:

        # Checks to see if the Value is a Value
        if value not in self.VALUES.keys():
            raise ValueError(f"{value} Enter is Not a Value")

        # Sets the Value
        self._value = value

    @property
    def suit(self) -> str:
        return self._suit

    @suit.setter
    def suit(self, suit:str) -> None:
        
        # Checks to see if Suit is a Suit
        if suit not in self.SUITS:
            raise ValueError(f"{suit} is Not a Suit")

        # Sets the Suit 
        self._suit  = suit

    @property
    def trueValue(self) -> int:
        return self._trueValue

    @trueValue.setter
    def trueValue(self, value:int) -> None:

        # Intialize the trueValue to the Card Value
        if value is None:
            self._trueValue = self.VALUES[self.value]

        # Checks the value to see if it can be set to it
        elif (value > max(list(self.VALUES.values())) or 1 > value):
            raise ValueError(f"Can't be set to {value}")

        # Set the Card's Value
        else:
            self._trueValue = value
   
    def __str__(self):
        return f"{self.value.capitalize()} of {self.suit.capitalize()}s"

