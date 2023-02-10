from abc import ABC, abstractmethod
from curses import meta
from typing import List
from user import User
from split import Split


class ExpenseMetadata(ABC):

    def __init__(self, name: str, imgUrl: str, notes: str):
        self.notes = notes
        self.img = imgUrl
        self.name = name


class Expense(ABC):
    def __init__(self, id, amount: float, paidBy: User, splitList: List[Split], metadata: ExpenseMetadata):
        self.id = id
        self.amount = amount
        self.paidBy = paidBy
        self.splitList = splitList
        self.metadata = metadata

    def setList(self, splits: List[Split]):
        self.splitList = splits

    def getList(self):
        return self.splitList

    def get_id(self): return self.id

    def getAmount(self): return self.amount

    def setMeta(self, meta: ExpenseMetadata):
        self.metadata = meta

    def getMeta(self):
        return self.metadata

    @abstractmethod
    def validate(self):
        pass
