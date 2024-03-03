from Exceptions import *



class Player:
    from Card import Card
    
    def __init__(self, name:str, amount:float = 10000):
        from Hands import Hands
        self.name = name.capitalize()

        self.amount = amount

        self.hands = Hands()

        self.betAmount = 0

        self.isSurrender = False

    def _drawCard(self, card:Card, handIndex:int = 0) -> None:
        hand = self.hands.get(handIndex)
        hand.drawCard(card)

    def _resetHands(self):
        self.hands.reset()

    def setBetAmount(self, value:float):

        # Checks to see if the Value is not negative or over the amount of money player has
        if 0 > value or value > self.amount:
            raise BetError

        self.betAmount = value

    def hit(self, card:Card, handIndex:int = 0):
        self._drawCard(card, handIndex)

    def doubleDown(self, card:Card, handIndex:int = 0):
        self.setBetAmount(self.betAmount * 2)
        self._drawCard(card, handIndex)

    def stand(self):
        pass

    def surrender(self):
        self.setBetAmount(self.betAmount / 2)
        self.isSurrender = True

    def split(self,firstCard:Card, secondCard:Card, handIndex:int = 0):
        import sys

        try:
            firstHand  = self.hands.get(handIndex)

            if firstHand.get(0).value != firstHand.get(1).value:

                print("Can not Split")
                sys.exit(1)

            # Create New Hand
            self.hands.addHand()

            # Retrieve the Second Card to make new Hand
            card = firstHand.get(1)
            card.trueValue = None
            self.hands.get(handIndex).removeCard(card)
            self.hands.get(handIndex + 1).drawCard(card)

            # Reset the First Card Value
            self.hands.get(0).get(0).trueValue = None 

            self._drawCard(firstCard, handIndex)
            self._drawCard(secondCard, handIndex + 1)

        except Exception as e:
            print(e)


    def win(self, winPercent:float = 1):
        self.amount += (self.betAmount * winPercent)

    def lose(self):
        self.amount -= self.betAmount

        if 0 > self.amount:
            raise AmountError

    def printHand(self, handIndex:int = 0):
        from Functions import printBar

        try:
            order ={0:"1st",1:"2nd",2:"3rd"}
            if self.hands.size() == 1:
                nameStatement = f"| {self.name}'s Hand |"
            
            elif handIndex in list(order.keys()):
                nameStatement = f"| {self.name}'s {order[handIndex]} Hand |"
            else:
                nameStatement = f"| {self.name}'s {handIndex + 1}th Hand |"


            printBar(len(nameStatement))
            print(nameStatement)
            printBar(len(nameStatement))

            for card in self.hands.get(handIndex).cards:
                print(f"- {card}")

            print()
            print(f"Value: {self.hands.get(handIndex).handValue()}\n\n")

        except Exception as e:
            print(e)


    














