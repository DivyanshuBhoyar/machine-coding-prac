from .user import User


class Split():

    def __init__(self, user: User):
        self._user = user

    def getUser(self):
        return self._user

    def setAmount(self, amount):
        self._amount = amount

    def getAmount(self):
        return self._amount
