from split import Split
from user import User


class EqualSplit(Split):
    def __init__(self, user: User):
        super().__init__(user)


class ExactSplit(Split):
    def __init__(self, user: User, amount: float):
        super().__init__(user)
        self.amount = amount


class PercentSplit(Split):
    def __init__(self, user: User, prc: float):
        super().__init__(user)
        self.percent = prc

    def getPercent(self):
        return self._percent

    def setPercent(self, percent):
        self.percent = percent
