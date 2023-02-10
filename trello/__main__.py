from models.user import User
from models.app import TrelloApp
from models.utils import Utils



USERS = [
    User("user1", "user1@email.com"),
    User("user2", "user2@email.com"),
    User("user3", "user3@email.com")
]


def main() : 
    app = TrelloApp()
    app.setUsers(USERS)
    
    while True :
        cmd = input("> Enter command...\n").split()
        ctype, cargs = cmd[0], cmd[1:]

        if ctype == "EXIT" :
            print("goodbye...")
            return
        elif ctype == "BOARD" :
            Utils.handle_board_cmd(app, cargs)
        elif ctype == "LIST" :
            Utils.handle_list_cmd(app, cargs)
        elif ctype == "CARD" :
            Utils.handle_card_cmd(app, cargs)
        elif ctype == "SHOW" :
            Utils.handle_show_cmd(app, cargs)
        else :
            print("plz try one of the available cmd")
    


if __name__ == "__main__":
    main()