

class Hands:
    from Hand import Hand
    def __init__(self):
        from Hand import Hand
        self.hands = [Hand()]

    def addHand(self):
        from Hand import Hand
        self.hands.append(Hand())

    def removeHand(self, hand:Hand ):
        self.hands.remove(hand)

    def reset(self):
        from Hand import Hand
        self.hands = [Hand()]

    def get(self, index:int) -> Hand:
        if self._isIn(index):
            return self.hands[index]
        else:
            raise IndexError

    def _isIn(self, index:int) -> bool:

        # Checks to see if it is a Valid Index in the hands
        if index > (len(self.hands) - 1):
            raise IndexError

        return True

    def __iter__(self):
        self._iter = 0
        return self

    def __next__(self):
        i = self._iter
        self._iter += 1;
        
        if i < len(self.hands):
            return self.hands[i]
        raise StopIteration

    def size(self) ->int:
        return len(self.hands)




