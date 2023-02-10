from models.board import Board
from models.dice import Dice


class Player():
    def __init__(self, name):
        self.name = name
        self.pos = 0 # postion of individual player
        self.win_status = False

    def get_pos(self):
        return self.pos

    def set_pos(self, newpos):
        self.pos = newpos
        return self.pos

    def get_win_status(self):
        return self.win_status

    def set_win_status(self, newstatus):
        self.win_status = newstatus
        return newstatus

    def play(self, dice: Dice, board: Board):
        cur_pos = self.get_pos()
        drw = dice.draw()
        new_pos = board.get_new_pos(cur_pos + drw)

        if new_pos != -1:
            self.set_pos(new_pos)
        else:
            print(
                f"Player {self.name} rolled a {drw} but could not move from {self.pos}")
            return

        print(
            f"Player {self.name} rolled a {drw} and moved from {cur_pos} to {new_pos}")
