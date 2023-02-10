from random import randint


class Dice():
    def __init__(self, faces):
        self.faces = faces
        print("init dice with ", faces)

    def draw(self):
        total = 0
        moves = 0

        while True:
            cur = randint(1, self.faces)
            moves += 1

            if cur != self.faces:
                return total + cur

            if moves == 3:
                return 0

            total += cur
            print("another turn")
