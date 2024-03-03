



class BlackJack:
    def __init__(self) -> None:
        self._player = Player('Player 1', 1000)
        self._dealer = None
        self._deck = Shoe()
        
        
    def deal(self) -> None:
        for x in range(2):
            self._player._hands[0].addCard(self._deck.drawCard())
            self._dealer._hand.addCard(self._deck.drawCard())
    
    def play(self) -> None:
        
        while(True):
            print("_______Welcome__BlackJack________")
            self.deal()
            
            print(self._player)
            print(self._dealer)
            
            for hand in self._player._hands:
                print("1. Hit")
                print("2. Stand")
                print("3. Split")
                print("4. Double Down")
                anwser = int(input("What do you want to do? "))
                
                if anwser == 1:
                    self._player.hit()
                elif anwser == 2:
                    self._player.stand()
                elif anwser == 3:
                    self._player.split()
                elif anwser == 4:
                    self._player.doubleDown()
                else:
                    raise KeyError()
                
                
            
            
            
            
            
            
    
    def __str__(self) -> str:
        return "Black Jack Game"
    
   
   
SUITES = {"Diamonds","Hearts","Spades","Clubs"} 
VALUES = {"Ace":11,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10}


class Card:
    def __init__(self, suite:str, value:str) -> None:
        self._suite = suite
        self._value = value
        self._trueValue = SUITES.get(self._value)
        
    @property
    def trueValue(self) -> int:
        return self._trueValue
    
    def __str__(self) -> str:
        return f"{self._value} of {self._value}"
       
    
class Shoe:
    def __init__(self, numDecks:int = 7) -> None:
        
        # Number of Decks
        self._numDecks = numDecks
        
        
        # Creation of the Cards
        self._cards = []
        for i in range(numDecks):
            self._cards.extend(self._createDeck())
        
        # Shuffle the Cards
        self.shuffle()
       
    @property
    def cards(self) -> list[Card]:
        return self._cards 
          
    def _createDeck(self) -> list[Card]: 
        
        cards = []
        for suite in SUITES:
            for value in list(VALUES.keys()):
                cards.append(Card(suite,value))
                
        return cards
    
    def shuffle(self) -> None:
        from random import shuffle
        
        shuffle(self._cards)
    
    def drawCard(self) -> Card:
        try:    
            card = self._cards.pop()
            
        except IndexError:
            for i in range(self._numDecks):
                self._cards.extend(self._createDeck())
                
            self.shuffle()
                
            card = self._cards.pop()
            
        return card
            
    
    
class Hand:
    def __init__(self) -> None:
        self._cards:list[Card] = []
        
    def addCard(self, card:Card) -> None:
        self._cards.append(card)
        
    def reset(self) -> None:
        self._cards = []
    
    @property
    def handValue(self) -> int:
        value = 0
        for card in self._cards:
            value += card.trueValue
            
            if value >= 21 and card._value == 'Ace':
                card._trueValue -=10
                value-=10
    
    
    
    
    
class Player:
    def __init__(self, name:str, amount:float):
        self._name  = name
        
        self._amount = amount
        
        self._hands = [Hand()]
        
    def doubleDown(self, hand:Hand, cards:Shoe):
        pass
    
    def stand(self, hand:Hand, cards:Shoe):
        pass
    
    def split(self, hands:list[Hand], hand:Hand, cards:Shoe):
        
        
        cardOne = hand._cards[0]
        cardTwo = hand._cards[1]
        hands.remove(hand)
        
        newOneHand = Hand()
        newOneHand.addCard(cardOne)
        newOneHand.addCard(cards.drawCard())
        
        newTwoHand = Hand()
        newTwoHand.addCard(cardTwo)
        newTwoHand.addCard(cards.drawCard())
        
        
        
        
        
    
    def hit(self, hand:Hand, cards:Shoe):
        hand.addCard(cards.drawCard())
    
    
    
    
    
    
    def __str__(self) -> str:
        s = f"{self._name}'s Hands: "
        
        for i, hand in enumerate(self._hands):
            s += f"Hand {i+1}: "
            for x, card in enumerate(hand._cards):
                if x != (len(hand)-1):
                    s += str(card)+", "
                else:
                    s += str(card)+"\n"
                    
        return s
                    
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    