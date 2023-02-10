from models.split_types import EqualSplit, ExactSplit, PercentSplit
from expense import Expense


class EqualExpense(Expense):
    def __init__(self, amt, id, by, splitList, meta):
        super().__init__(id, amt, by, splitList, meta)

    def validate(self):
        for split in self.splitList:
            if not isinstance(split, EqualSplit):
                return False
        return True


class ExactExpense(Expense):
    def __init__(self, amt, id, by, splitList, meta):
        super().__init__(id, amt, by, splitList, meta)

    def validate(self):
        for s in self.splitList:
            if not isinstance(s, ExactSplit):
                return False

        sum = 0
        tar = self.getAmount()

        for s in self.splitList:
            sum += s.getAmount()

        return sum == tar


class PercentExpense(Expense):
    def __init__(self, amt, id, by, splitList, meta):
        super().__init__(id, amt, by, splitList, meta)

    def validate(self):

        for s in self.splitList:
            if not isinstance(s, PercentSplit):
                return False

        sm = 0
        for s in self.splitList:
            sm += PercentSplit(s)
