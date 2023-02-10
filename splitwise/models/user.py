class User:
    def __init__(self, name, email, phone, id):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__id = id

    def getName(self):
        return self.__name

    def setName(self, name):
        return self.__name

    def getId(self):
        return self.__id
