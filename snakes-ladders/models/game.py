from models.dice import Dice
from models.board import Board
from models.player import Player


class Game():

    def __init__(self, die_faces, size):
        self.dice = Dice(die_faces)
        self.board = Board(size)
        self.winners = []
        self.players = {}
        self.active_players = 0

# call board methods for each single one, board has other instances too
    def set_snakes(self, snakes):
        for snake in snakes:
            try:
                self.board.set_snake_pos(snake)
            except:
                continue

    def set_ladders(self, ladders):
        for ladder in ladders:
            try:
                self.board.set_ladder_pos(ladder)
            except:
                continue

#  save a new player instance to state 
    def set_players(self, players):
        self.active_players = len(players)
        if self.active_players < 2:
            raise Exception("Min two players required")

        for p in players:
            self.players[p] = Player(p)

        print("set players", self.players)

    def set_winners(self, player: Player):
        self.winners.append(player)
        self.active_players -= 1

    def play_game(self):
        while True:
            for _, player in self.players.items():
                if not player.get_win_status():
                    player.play()
                    if self.board.
