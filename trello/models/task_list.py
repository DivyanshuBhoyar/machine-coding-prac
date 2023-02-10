from typing import List
from uuid import uuid4

from .card import Card

class TaskList :
    def __init__(self, name, board) :
        self.name = name
        self.id = str(uuid4())
        self.cards = {}
        self.board = board
    
    
    def set_name(self, name) :
        self.name = name
    
    def create_card(self, card: Card):
        self.cards[card.id] = Card
    
    def rmv_card(self, card: Card):
        self.cards.pop(card.id)

