from Functions import printBar

class BlackJack:
    from Player import Player

    def __init__(self):
        from Deck import Deck
        from Dealer import Dealer
        
        self.intro()
        self.players = self.setPlayers()
        self.dealer = Dealer()
        self.deck = Deck()
        self._loop()
        self.end()

    def intro(self):
        print()
        print("---------- Welcome to Black Jack Game ----------")
        print()

    def end(self):
        print()
        print("---------- Game Over ----------")
        print()

    def setPlayers(self) -> list[Player]:
        from Player import Player

        # List to Stor the Players
        players = []
        
        # Get the Amount of Players
        while True:
            try:

                amountPlayers = int(input("How many Players (max 6)? "))
                print()

                if amountPlayers > 6 or 0 >= amountPlayers:
                    raise ValueError

                break
            except ValueError:

                # Try Again
                print()
                print("Try Again")
                print()

        printBar(48)
        print()


        # Get each Player Set
        for x in range(amountPlayers):

            
            # Get Player's Name
            while True:
                try:

                    playerName = input(f"Player {x+1}'s Name: ").capitalize()
                    print()

        
                    break

                except TypeError:

                    print("Try Again")
                    print()


            # Set the Amount a Money Player has
            while True:
                try:
                    # Get the Amount of Money Player has
                    amount = float(input(f"{playerName}'s Amount of Money: $"))
                    print()

                    if 0 >= amount:
                        raise ValueError

                    break

                except ValueError:

                    # Try Again
                    print("Try Again")
                    print()
            

            # Setting Player and Adding Player to Players
            players.append(Player(playerName, amount))

            printBar(48)
            print()

        return players

    def _drawCard(self, player:Player, handIndex:int = 0):
        player._drawCard(self.deck.drawCard(),handIndex)

    def _removePlayer(self, player:Player):
        # Removing Broke Players
        if player.amount == 0:
            print(f"{player.name} has run out of money and is kicked from the Game.")
            self.players.remove(player)

    def _setBetAmount(self, player:Player):
        # Bet Amount Set
        while True:
            try:
                bet = float(input("How much you want to bet? $"))
                print()

                if (bet > player.amount or 0 >= bet):
                    raise ValueError

                break
            except ValueError:
                print("Try Again")
                print()

        player.setBetAmount(bet)

    def _setBets(self):
        # Setting Bets for Players and Removing the Broke the Players
        for player in self.players:

            # Removing Broke Players
            self._removePlayer(player)


            # Prints the Player's Name and their Money Amount
            print(f"------------ {player.name} ------------")
            print(f"Account: ${player.amount}\n")
                

            # Bet Amount Set
            self._setBetAmount(player)
    
    def _keepPlaying(self):
        # Ask if they want to Continue or Quit
        for player in self.players:
            print(f"------------ {player.name} ------------")
            print()

            while True:
                try:
                    playInput = input("Do you want to keep playing (y/n)? ").lower()
                    print()
                    
                    if (playInput != "n") and (playInput != "y"):
                        raise TypeError

                    break
                except TypeError:
                    print("Try Again")
                    print()
           
            if playInput == "n":
                self.players.remove(player)
            continue

    def _initDeal(self):
        # Deals out Cards
        for x in range(2):
            for player in self.players:
                self._drawCard(player)

            self.dealer._drawCard(self.deck.drawCard())

    def _playerPlay(self):
        # Iterate through the Players
        for player in self.players:

            # Iterate through the Hands of the Player
            i = 0
            while i < player.hands.size():

                # Current Hand
                hand = player.hands.get(i)

                # X is the Counter of How many times the player call an action on the hand
                x = 0

                # Anwser is the Reponse on Action Player will take
                anwser = None

                # Player has Black Jack Hand
                if (i == 0) and hand.handValue() == 21 and player.hands.size() == 1:
                    continue


                # Go through Hand until Hand Value goes over 21 or Action is Stand
                while((21 >= hand.handValue())):

                    # Prints the Dealer's and the Player's Hands
                    self.dealer.printHand(False)
                    player.printHand(i)

                    # Asks if this is the First Action and if the Player can Split

                    if ((x==0) and (self.dealer.hand.handValue(False) == 11)):

                        while True:
                            try:
                                insuranceAnwser = input("Do you want insurance (y/n)? ").lower()
                                
                                if insuranceAnwser not in ["y","n"]:
                                    raise TypeError
                                print()
                                break
                            except TypeError:
                                print()
                                print("Try Again")
                                print()












                    elif (x == 0) and(hand.size() == 2) and(hand.get(0).value == hand.get(1).value):
                        while True:
                            try:
                                anwser = input("Split (sp), Double Down (dd), Hit (h), Stand(st), or Surrender (s): ")
                                print()

                                if (anwser != "sp") and (anwser != "dd") and (anwser != "h") and (anwser != "st") and (anwser != "s"):
                                    raise TypeError

                                break
                            except TypeError:
                                print("Try Again")
                                print()

                    elif (x == 0):
                        while True:
                            try:
                                anwser = input("Double Down (dd), Hit (h), Stand(st), or Surrender (s): ")
                                print()

                                if (anwser != "dd") and (anwser != "h") and (anwser != "st") and (anwser != "s"):
                                    raise TypeError

                                break
                            except TypeError:
                                print("Try Again")
                                print()

                    else:
                        while True:
                            try:
                                anwser = input("Hit (h), Stand(st), or Surrender (s): ")

                                if (anwser != "h") and (anwser != "st") and (anwser != "s"):
                                    raise TypeError

                                break
                            except TypeError:
                                print("Try Again")
                                print()

                    print()
                    # Splitting the Cards
                    if anwser == "sp" and x == 0 and (hand.get(0).value == hand.get(1).value):
                        player.split(self.deck.drawCard(),self.deck.drawCard(),i)
                        x -= 1

                    # Doubling Down
                    elif anwser == "dd" and x == 0:
                        player.doubleDown(self.deck.drawCard(),i)
                        break

                    # Hit
                    elif anwser == "h":
                        player.hit(self.deck.drawCard(),i)

                    # Surrender
                    elif anwser == "s":
                        player.surrender()
                        break

                    # Stand
                    elif anwser == "st":
                        break

                    else:
                        raise ValueError(f"{anwser} is not an Option")
                        
                    anwser = None
                    x+=1


                i += 1

    def _isAllPlayerSet(self):
        # Checking the Players to see if all the Players went Set
        for player in self.players:
            for hand in player.hands:
                if 21 >= hand.handValue():
                    return False    
           
        return True

    def _winsLoses(self):
        # Print Wins and Loses of each Player
        for player in self.players:

            # Goes through each Hand of the Player
            for z, hand in enumerate(player.hands):

                # Prints the Dealer's and Player's Hand
                self.dealer.printHand()
                player.printHand(z)
                
                #  Player went Over 21 or Surrendered: Player Lose
                if hand.handValue() >= 22 or  player.isSurrender == True:

                    print(f"{player.name} Lost ${player.betAmount}")
                    print()
                    player.lose()
                    player.isSurrender = False

                # Player got a Black Jack
                elif hand.handValue() == 21 and (len(hand.cards) == 2):
                    print("Winner Winner Chicken Dinner !!")
                    print(f"{player.name} Won ${player.betAmount * 1.5}")
                    print()
                    player.win(1.5)

                # Dealer went Over 21: Player Win
                elif  self.dealer.hand.handValue() >= 22:
                    print(f"{player.name} Won ${player.betAmount}")
                    print()
                    player.win()

                # Dealer hand Bigger Hand than Player: Player Lose
                elif self.dealer.hand.handValue() > hand.handValue():
                    print(f"{player.name} Lost ${player.betAmount}")
                    print()
                    player.lose()
                    player.isSurrender = False

                # Dealer and Player have the same Hand Value
                elif hand.handValue() == self.dealer.hand.handValue():
                    print(f"{player.name} Push, No Win or Lose")

                # Player's Hand was Better than Dealer's
                else:
                    print(f"{player.name} Won ${player.betAmount}")
                    print()
                    player.win()

            # Reset the Player's Hands
            player.hands.reset()

    def _loop(self):
        while self.players != []:

            # Sets the Bets of Players and Removes Broke Players
            self._setBets()

            # Deal intial Cards two cards to each player
            self._initDeal()
            
            # Iterate through the Players
            self._playerPlay()

            # Dealer's Turn to Draw Cards if the Players did not Go Set
            while(17 > self.dealer.hand.handValue() and self._isAllPlayerSet() == False):
                self.dealer.hit(self.deck.drawCard())

            # Print Wins and Loses of each Player
            self._winsLoses()

            # Keep Playing?
            self._keepPlaying()
            
            # Reset the Dealer's Hand
            self.dealer.hand.reset()

                    


               
BlackJack()
            

            



