from uuid import uuid4

from models.user import User
from models.task_list import TaskList

class Board :
    def __init__(self, name: str, creator_id: str) :
        self.name = name
        self.id: str = str(uuid4())
        self.privacy: "PUBLIC" | "PRIVATE" = "PUBLIC"
        self.members = set([creator_id])
        self.lists = {}
    
    
    def set_privacy(self, prvc) :
        self.privacy = prvc
    
    def setName(self, name):
        self.name = name
    
    def add_member(self, member: User):
        self.members.add(member)
        print("member added: ", member.name)

    def rmv_member(self, member: User):
        self.members.discard(member)
        print("member removed: ", member.name )
    
    def add_list(self, lst : TaskList):
        self.lists[lst.id] = lst
        print(f'new list {lst.id} added to board ', self.id)

    def delete_list(self, lst_id: str):
        lst = self.lists.get(lst_id) 
        if lst :
            del self.lists[lst_id]
        del lst