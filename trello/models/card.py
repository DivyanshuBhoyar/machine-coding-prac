from uuid import uuid4

class Card :
    def __init__(self, name: str, descr: str, lst_id: str ) :
        self.name = name
        self.id = str(uuid4())
        self.assigned_user = None
        self.description = None
        self.list_id = lst_id


    def assign_user(self, user_email) :
        self.assigned_user = user_email
    
    def unassign(self):
        self.assign_user = None

    def set_description(self, descr: str) :
        self.description = descr
    
    def set_name(self, name: str):
        self.name  = name 
    
    def unassign(self) : self.assigned_user = None

    def move(self, list_id: str):
        self.list_id = list_id
