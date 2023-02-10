from typing import List
from pprint import pprint 


from .app import TrelloApp
from .board import Board
from .task_list import TaskList
from .card import Card


def fmtprint(data) : pprint(data)
def is_valid_uuid(id_str) : 
    return len(id_str) == 36 if not Utils.use_debug else len(id_str) in [2, 36]

class Utils :
    use_debug = True


    @staticmethod
    def handle_board_cmd(app: TrelloApp, args : List[str]):
        arg0 = args[0]

        if arg0 == "CREATE" : 
            name = args[1]
            if name : 
                new_board = Board(name, "ADMIN")
                app.save_board(new_board)

                if Utils.use_debug :   # debug_only
                    app.boards[new_board.name] = new_board

        elif arg0 == "DELETE":
            b_id = args[1]
            app.delete_board(b_id)
        
        elif len(args) == 3 and is_valid_uuid(arg0):  # can be a uuid, basic validator
            cmd, arg2 = args[1], args[2]            
            board = app.get_board(arg0)
            
            if not board: 
                print("not found")
                return

            if cmd == "NAME" : board.setName(arg2)
            
            if cmd == "PRIVACY" : 
                if arg2 not in ['PUBLIC', 'PRIVATE'] : 
                    print("invalid value")
                    return
                board.set_privacy(arg2)

            if cmd == "ADD_MEMBER" : 
                mem = app.get_user(arg2)
                if not mem : 
                    print("no user found")
                    return
                board.add_member(mem)

            if cmd == "REMOVE_MEMBER" : 
                mem = app.get_user(arg2)
                if mem :
                    board.rmv_member(mem)
    

    @staticmethod
    def handle_show_cmd(app: TrelloApp, args: List[str]):
        if not args :
            data = [vars(v) for k, v in app.get_boards().items()]
            fmtprint(data)
        
        elif args[0] == "USERS" :
            data = [vars(v) for k, v in app.get_users().items()]
            fmtprint(data)
        
        elif args[0] == 'BOARD' and is_valid_uuid(args[1]) : 
            data = vars(app.get_board(args[1]))
            fmtprint(data)
        
        elif args[0] == "LIST" and is_valid_uuid(args[1]) :
            data = app.get_list(args[1])
            if not data : print({})
            else : fmtprint(vars(data))

        elif args[0] == "CARD" and is_valid_uuid(args[1]) :
            data = vars(app.get_card(args[1]))
            fmtprint(data)
    

    @staticmethod
    def handle_list_cmd(app: TrelloApp, args: List[str]):
        arg0 = args[0]

        if arg0 == 'CREATE' and  len(args) == 3:
            b_id, name = args[1], args[2]

            if b_id not in app.get_boards() : 
                print("board not found")
                return
            
            board = app.get_board(b_id)
            new_list = TaskList(name, board)
            board.add_list(new_list)  # add to specific board
            app.save_list(new_list)   # save ref to app

            if Utils.use_debug :      # debug_only
                app.lists[new_list.name] = new_list            
            

        if arg0 == "DELETE":  
            l_id = args[1]
            boardref : Board = app.get_list(l_id).board
            boardref.delete_list(l_id)
            app.rmv_list(l_id)

        if is_valid_uuid(arg0) and args[1] == "NAME" and len(args) == 3 :
            lst = app.get_list(arg0)
            name = args[2]
            if lst :
                lst.set_name(name)
            else : print("list not found")
            return
        
    
    @staticmethod
    def handle_card_cmd(app: TrelloApp, args: List[str]):
        arg0 = args[0]
        
        #create
        if arg0 == "CREATE" and len(args) == 3 :
            lst_id, name = args[1], args[2]
            lst = app.get_list(lst_id)
            if not lst : 
                print("list not found")
                return
            
            card = Card(name, None, lst_id)
            lst.create_card(card)
            app.save_card(card)
            print("created card: ", card.id)

            if Utils.use_debug :   # debug_only
                app.cards[card.name] = card               
        
        # rename
        if is_valid_uuid(arg0) and len(args) == 3 and args[1] == 'NAME':
            c_id = arg0
            card = app.get_card(c_id)

            if card : 
                name = args[2]
                card.set_name(name)
                print("renamed")

            else : print("card not found") 

        # set description
        if is_valid_uuid(arg0) and len(args) == 3 and args[1] == 'DESCRIPTION':
            c_id = arg0
            card = app.get_card(c_id)

            if card : 
                descr = args[2]
                card.set_description(descr)
                print("description added")

            else : print("card not found")
        
        #assign
        if is_valid_uuid(arg0) and len(args) == 3 and args[1] == "ASSIGN":
            card = app.get_card(arg0)
            if card :
                user = app.get_user(args[2])
                if not user : return
                card.assign_user(user.email)
                print("assigned user")
            else :
                print("card not found")

        
        #unassign
        if is_valid_uuid(arg0) and len(args) == 2 and args[1] == "UNASSIGN" :
            card = app.get_card(arg0)
            if card :
                card.unassign()
                print("unassigned")

        #move
        if is_valid_uuid(arg0) and len(args) == 3 and args[1] == "MOVE" :
            card = app.get_card(arg0)

            if card :
                new_list = app.get_list(args[2])
                old_list = app.get_list(card.list_id)
                if not new_list or new_list.board.id != old_list.board.id :
                    print("list not found or boards mismatch")
                    return
                
                card.move(new_list.id)
                old_list.rmv_card(card)
                new_list.create_card(card)
                print("moved")
