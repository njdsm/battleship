from fleet import Fleet


class Player:
    def __init__(self, name):
        self.name = name
        self.remaining_ships = {"destroyer": 2, "submarine": 3}
        self.fleet = Fleet()
        self.rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.columns = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.my_board = [{"A1": "O", "A2": "O", "A3": "O", "A4": "O", "A5": "O",
                          "A6": "O", "A7": "O", "A8": "O", "A9": "O", "A10": "O"},
                         {"B1": "O", "B2": "O", "B3": "O", "B4": "O", "B5": "O",
                          "B6": "O", "B7": "O", "B8": "O", "B9": "O", "B10": "O"},
                         {"C1": "O", "C2": "O", "C3": "O", "C4": "O", "C5": "O",
                          "C6": "O", "C7": "O", "C8": "O", "C9": "O", "C10": "O"},
                         {"D1": "O", "D2": "O", "D3": "O", "D4": "O", "D5": "O",
                          "D6": "O", "D7": "O", "D8": "O", "D9": "O", "D10": "O"},
                         {"E1": "O", "E2": "O", "E3": "O", "E4": "O", "E5": "O",
                          "E6": "O", "E7": "O", "E8": "O", "E9": "O", "E10": "O"},
                         {"F1": "O", "F2": "O", "F3": "O", "F4": "O", "F5": "O",
                          "F6": "O", "F7": "O", "F8": "O", "F9": "O", "F10": "O"},
                         {"G1": "O", "G2": "O", "G3": "O", "G4": "O", "G5": "O",
                          "G6": "O", "G7": "O", "G8": "O", "G9": "O", "G10": "O"},
                         {"H1": "O", "H2": "O", "H3": "O", "H4": "O", "H5": "O",
                          "H6": "O", "H7": "O", "H8": "O", "H9": "O", "H10": "O"},
                         {"I1": "O", "I2": "O", "I3": "O", "I4": "O", "I5": "O",
                          "I6": "O", "I7": "O", "I8": "O", "I9": "O", "I10": "O"},
                         {"J1": "O", "J2": "O", "J3": "O", "J4": "O", "J5": "O",
                          "J6": "O", "J7": "O", "J8": "O", "J9": "O", "J10": "O"}]
        self.opponent_board = [{"A1": "O", "A2": "O", "A3": "O", "A4": "O", "A5":
                            "O", "A6": "O", "A7": "O", "A8": "O", "A9": "O", "A10": "O"},
                         {"B1": "O", "B2": "O", "B3": "O", "B4": "O", "B5": "O",
                          "B6": "O", "B7": "O", "B8": "O", "B9": "O", "B10": "O"},
                         {"C1": "O", "C2": "O", "C3": "O", "C4": "O", "C5": "O",
                          "C6": "O", "C7": "O", "C8": "O", "C9": "O", "C10": "O"},
                         {"D1": "O", "D2": "O", "D3": "O", "D4": "O", "D5": "O",
                          "D6": "O", "D7": "O", "D8": "O", "D9": "O", "D10": "O"},
                         {"E1": "O", "E2": "O", "E3": "O", "E4": "O", "E5": "O",
                          "E6": "O", "E7": "O", "E8": "O", "E9": "O", "E10": "O"},
                         {"F1": "O", "F2": "O", "F3": "O", "F4": "O", "F5": "O",
                          "F6": "O", "F7": "O", "F8": "O", "F9": "O", "F10": "O"},
                         {"G1": "O", "G2": "O", "G3": "O", "G4": "O", "G5": "O",
                          "G6": "O", "G7": "O", "G8": "O", "G9": "O", "G10": "O"},
                         {"H1": "O", "H2": "O", "H3": "O", "H4": "O", "H5": "O",
                          "H6": "O", "H7": "O", "H8": "O", "H9": "O", "H10": "O"},
                         {"I1": "O", "I2": "O", "I3": "O", "I4": "O", "I5": "O",
                          "I6": "O", "I7": "O", "I8": "O", "I9": "O", "I10": "O"},
                         {"J1": "O", "J2": "O", "J3": "O", "J4": "O", "J5": "O",
                          "J6": "O", "J7": "O", "J8": "O", "J9": "O", "J10": "O"}]

    def display_board(self):
        print(f"{self.name}'s Board")
        i = 0
        print("   1 2 3 4 5 6 7 8 9 10")
        while i < len(self.my_board):
            val = str(self.my_board[i].values())
            val = val[14:-3]
            x = ''.join(c for c in val if c not in "',")
            print(self.rows[i] + "  " + x)
            i += 1
        print("\n")

    def display_remaining_ships(self):
        val = str(self.remaining_ships.keys())
        val = val[11:-3]
        x = ''.join(c for c in val if c not in "'")
        print(f"{self.name}'s remaining ships: {x}\n")

    def validate_input(self, i):
        choice = input(f"Where would you like to put {i.name} length {i.size}"
                       f"\n:").capitalize()
        if choice[0] in self.rows and choice[1:] in self.columns:
            if self.my_board[self.rows.index(choice[0])][choice] != "S":
                return [choice, False]
            else:
                print("You already have a ship in that space.")
                return ['', True]
        else:
            return ['', True]

    def input_loop(self, i):
        choice = ['', True]
        while choice[1]:
            choice = self.validate_input(i)
            if choice[0] != '':
                choice[1] = False
            else:
                print("Not a valid option")
        #choice = choice[0]
        return choice[0]

    def setup_board(self, placed_ships):
        for i in self.fleet.ships:
            if i not in placed_ships:
                choice = self.input_loop(i)
                direction = self.get_direction()
                i.spaces = self.validate_direction(choice, direction, i.size)
                if not i.spaces:
                    self.display_board()
                    print("Not a valid direction to place your ship, Let's try again.")
                    self.setup_board(placed_ships)
                else:
                    self.place_ship(i.spaces)
                placed_ships.append(i.name)

    def get_direction(self):
        try:
            direction = int(input("From that point, which way should the ship go:"
                                  " \n1: up\n2: down\n3: left\n4: right\n:"))
            assert 0 < direction <= 4
        except:
            print("pick one of the numbers")
            direction = self.get_direction()
        return direction

    # This function will check each space the user wants the ship to occupy, if there is already a ship or if it is off
    # the board, it will return false. if it's valid it will return a list of the spaces the ship will occupy
    def validate_direction(self, choice, direction, ship_size):
        spaces = [choice]
        i = 1
        while i < ship_size:
            choice_temp = choice
            # Validate up
            if direction == 1:
                if self.rows.index(choice_temp[0]) - 1 < 0:
                    return False
                letter_index = self.rows.index(choice_temp[0]) - i
                choice_temp = self.rows[letter_index] + choice_temp[1:]
                if self.my_board[letter_index][choice_temp] == "S":
                    return False
                else:
                    spaces.append(choice_temp)
            # Validate down
            elif direction == 2:
                if self.rows.index(choice_temp[0]) + 1 > 9:
                    return False
                letter_index = self.rows.index(choice_temp[0]) + i
                choice_temp = self.rows[letter_index] + choice_temp[1:]
                if self.my_board[letter_index][choice_temp] == "S":
                    return False
                else:
                    spaces.append(choice_temp)
                    # self.my_board[letter_index][choice_temp] = "S"

            # Validate left
            elif direction == 3:
                number_from_choice = choice_temp[1:]
                number = int(number_from_choice) - i
                if number < 0:
                    return False
                choice_temp = choice_temp[0] + str(number)
                current_row = self.rows.index(choice_temp[0])
                if self.my_board[current_row][choice_temp] == "S":
                    return False
                else:
                    spaces.append(choice_temp)
                    #self.my_board[current_row][number] = "S"

            # Validate right
            elif direction == 4:
                number_from_choice = choice_temp[1:]
                number = int(number_from_choice) + i
                if number > 9:
                    return False
                choice_temp = choice_temp[0] + str(number)
                current_row = self.rows.index(choice_temp[0])
                if self.my_board[current_row][choice_temp] == "S":
                    return False
                else:
                    spaces.append(choice_temp)
            i += 1
        self.my_board[self.rows.index(choice[0])][choice] = "S"
        return spaces

    def place_ship(self, choices):
        for i in choices:
            row = self.rows.index(i[0])
            self.my_board[row][i] = "S"
        self.display_board()

    def turn_start(self):
        print(f"{self.name}'s turn!")
        self.display_board()
        self.display_opponent_board()
        guess = self.input_loop_player_guess()
        return guess

    def player_guess(self):
        choice = ""
        while choice == "":
            choice = input(f"Where would you like to check?"
                       f"\n:").capitalize()
        if choice[0] in self.rows and choice[1:] in self.columns:
            if self.opponent_board[self.rows.index(choice[0])][choice] != "X" and \
                    self.opponent_board[self.rows.index(choice[0])][choice] != "M":
                return [choice, False]
            else:
                print("You already guessed that space, try another one.")
                return ['', True]
        else:
            return ['', True]

    def input_loop_player_guess(self):
        choice = ['', True]
        while choice[1]:
            choice = self.player_guess()
            if choice[0] != '':
                choice[1] = False
            else:
                print("Not a valid option")
        # choice = choice[0]
        return choice[0]

    def hit_check(self, guess, opponent_board):
        row = self.rows.index(guess[0])
        if opponent_board[row][guess] == "S":
            print("Hit!")
            opponent_board[row][guess] = "X"
            self.opponent_board[row][guess] = "X"
        else:
            print("Miss!")
            self.opponent_board[row][guess] = "M"
        return opponent_board

    def display_opponent_board(self):
        i = 0
        print("   1 2 3 4 5 6 7 8 9 10")
        while i < len(self.opponent_board):
            val = str(self.opponent_board[i].values())
            val = val[14:-3]
            x = ''.join(c for c in val if c not in "',")
            print(self.rows[i] + "  " + x)
            i += 1
        print("\n")

    def ship_hit_check(self, guess):
        for i in self.fleet.ships:
            if guess in i.spaces:
                i.spaces.remove(guess)
                if len(i.spaces) == 0:
                    print(f"You sank their {i.name}!!!")

    # TODO refactor input_loop function line 80 and validate_input function line 68
    # will want strings to be set as variables that pass in.
    # will allow reuse of functions for player guesses and ship placement
