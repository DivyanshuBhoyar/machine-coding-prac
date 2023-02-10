from models.ladder import Ladder
from models.snake import Snake


class Board:
    def __init__(self, size):
        self.size = size
        self.board = {}

    def set_ladder_pos(self, ladder):
        if ladder[0] >= ladder[1] or ladder[0] == self.size:
            raise Exception("invalid postition")
        elif ladder[0] in self.board:
            raise Exception("Postion already occupied")
        else:
            self.board[ladder[0]] = Ladder(tuple(ladder))

    def set_snake_pos(self, snake):
        if snake[0] <= snake[1] or snake[0] == self.size:
            raise Exception("invalid postition")
        elif snake[0] in self.board:
            raise Exception("Postion already occupied")
        else:
            self.board[snake[0]] = Snake(tuple(snake))

    def get_new_pos(self, pos):
        if pos > self.size:
            return -1

        elif pos in self.board:
            return self.board[pos].end

        else:
            return pos

    def has_won(self, pos):
        return pos == self.size
