from typing import List


from .user import User
from .board import Board
from .task_list import TaskList
from .card import Card



class TrelloApp():
    
    def __init__(self) :
        self.users = {}
        self.boards = {}
        self.lists = {}
        self.cards = {}

    def setUsers(self, appUsers: List[User]):
        for u in appUsers :
            self.users[u.userId] = u
        
        print("users added")
    
    def save_board(self, board: Board) :
        self.boards[board.id] = board
        print("created with id: ", board.id)
    
    def delete_board(self, id: str):
        if id not in self.boards : print("not found")
        b_ref = self.boards[id]
        del self.boards[id]
        del b_ref
    
    def get_boards(self) :
        return self.boards
    
    def get_board(self, b_id: str) -> Board :
        return self.boards.get(b_id)

    def get_users(self) :
        return self.users
    
    def get_user(self, uid: str) -> User:
        return self.users.get(uid)
    
    def save_list(self, lst: TaskList):
        self.lists[lst.id] = lst
    
    def rmv_list(self, lst_id):
        del self.lists[lst_id]
    
    def get_list(self, lst_id) -> TaskList:
        return self.lists.get(lst_id)
    
    def save_card(self, card : Card) :
        self.cards[card.id] = card
    
    def get_card(self, c_id) -> Card:
        return self.cards.get(c_id)