from player import Player
import time
import shutil

class Game:
    def __init__(self):
        self.name = "Bad-leShip"
        self.player_one = Player("Player One")
        self.player_two = Player("Player Two")
        self.round = 0
        #self.size = shutil.get_terminal_size()

    def run_game(self):
        print("Welcome to Bad-leShip! It's just like the beloved childhood game, just not quite as fun.\n")
        self.player_one.name = input("Player One, what do you want your name to be?\n:")
        print(f"Great! Ok {self.player_one.name}, please pass the screen to Player Two. I'll give you some time...")
        counter = 5
        while counter > 0:
            print(counter)
            time.sleep(1)
            counter -= 1
        print("\n" * 100)
        self.player_two.name = input(f"Player Two, what do you want your name to be?\n"
                                     f"For example your friend chose {self.player_one.name}.\n:")
        self.display_boards()

    def display_boards(self):
        self.player_one.display_board()
        self.player_one.display_remaining_ships()
        self.player_two.display_board()
        self.player_two.display_remaining_ships()

    def player_one_turn(self):
        self.round += 1
        print(self.round)
        print("\n" * 24)
        #input