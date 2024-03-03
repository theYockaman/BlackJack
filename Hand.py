
class Hand:
    from Card import Card

    def __init__(self):
        self.cards = []

    def handValue(self, showAll:bool = True) -> int:
        if showAll:
            cards = self.cards
        else:
            cards = self.cards[1:]

        value = 0
        for card in cards:
            value += card.trueValue

        if value > 21:
            for card in cards:
                if card.trueValue == 11:
                    card.trueValue = 1
                    value -= 10
                    break

        return value

    def drawCard(self, card:Card) -> None:
        self.cards.append(card)

    def removeCard(self, card:Card) -> None:
        self.cards.remove(card)

    def reset(self) -> None:
        self.cards = []

    def get(self, index:int) -> Card:
        return self.cards[index]

    def size(self) -> int:
        return len(self.cards)

    def isEmpty(self) -> bool:
        return True if (self.cards == []) else False

    def __iter__(self):
        self._iter = 0
        return self

    def __next__(self):
        i = self._iter
        self._iter += 1;

        if i < len(self.cards):
            return self.cards[i]
        raise StopIteration

