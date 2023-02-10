from uuid import uuid4



class User :
    def __init__(self, name: str, email:str) :
        self.name = name
        self.email = email
        self.userId = str(uuid4())

    def getDetails(self) :
        print(vars(self))