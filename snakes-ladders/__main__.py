from models.game import Game


def game_manger(snakes, ladders, players, faces, size):
    game = Game(faces, size)
    game.set_ladders(ladders)
    game.set_snakes(snakes)
    game.set_players(players)
    print("\n--Game is ready to start--\n")
    game.play_game()


def main():
    snakes = []
    ladders = []
    players = []

    no_faces = int(input("Number of faces"))

    no_snakes = int(input("Enter number of snakes"))
    print(f"Enter {no_snakes} lines of snake input")
    for _ in range(no_snakes):
        data = tuple(map(int, input().split()))
        snakes.append(data)

    no_ladders = int(input("Enter the number of ladders"))
    print("Enter ladders data")
    for _ in range(no_ladders):
        data = tuple(map(int, input().split()))
        ladders.append(data)

    no_players = int(input("Enter number of players"))
    if no_players < 2:
        print("min players req is 2")

    print(f"Enter no_players names")
    for _ in range(no_players):
        players.append(input())

    game_manger(snakes, ladders, players, no_faces, size=100)


if __name__ == "__main__":
    main()

'''
- Number of snakes (s) followed by s lines each containing 2 numbers denoting the head and tail positions of the snake.
- Number of ladders (l) followed by l lines each containing 2 numbers denoting the start and end positions of the ladder.
- Number of players (p) followed by p lines each containing a name.
'''
