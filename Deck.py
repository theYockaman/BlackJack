




class Deck:
    from Card import Card
    VALUES = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"jack":10,"queen":10,"king":10,"ace":11}
    SUITS = ["club","spade","diamond","heart"]
    
    def __init__(self, shoeSize:int = 7):

        self.shoeSize = shoeSize

        self.cards = self.createCards()

    @property
    def shoeSize(self):
        return self._shoeSize

    @shoeSize.setter
    def shoeSize(self, shoeSize:int):
        
        # Check if the Shoe Size is Valid
        if 0 >= shoeSize:
            raise ValueError(f"{shoeSize} is not a Shoe Size")

        self._shoeSize = shoeSize

    def createCards(self) -> list:
        from Card import Card
        from random import shuffle

        cards = []
        for x in range(self.shoeSize):
            for suit in self.SUITS:
                for value in self.VALUES.keys():
                    cards.append(Card(value,suit))

        shuffle(cards)
        return cards

    def drawCard(self) -> Card:
        if self.cards == []:
            self.cards = self.createCards()
        
        card = self.cards[0]
        self.cards.pop(0)

        return card














