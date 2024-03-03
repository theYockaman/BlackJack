

class Dealer:
    from Card import Card
    def __init__(self):
        from Hand import Hand
        self.name = "Dealer"

        self.hand = Hand()

    def _drawCard(self, card:Card):
        self.hand.drawCard(card)

    def hit(self, card:Card):
        self._drawCard(card)

    def stand(self):
        pass

    def printHand(self, showAll:bool = True):
        from Functions import printBar
        if showAll:
            cards  = self.hand.cards
        else:
            cards = self.hand.cards[1:]

        nameStatement = f"| {self.name}'s Cards |"
        printBar(len(nameStatement))
        print(nameStatement)
        printBar(len(nameStatement))
        
        for card in cards:
            print(f"- {card}")
        print()
        print(f"Value: {self.hand.handValue(showAll)}\n\n\n")
        






