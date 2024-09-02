class Game:
    def __init__(self, turn, tie, winner, board):
        self.turn = "X"
        self.tie = False
        self.winner = None
        self.board = {
            "a1": None,
            "b1": None,
            "c1": None,
            "a2": None,
            "b2": None,
            "c2": None,
            "a3": None,
            "b3": None,
            "c3": None,
        }

    def play_game(self):
        print("Shall we play a game?")

    def print_board(self):
        b = self.board
        print(
            f"""
              A   B   C
          1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
              ----------
          2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
              ----------
          3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """
        )

    def print_message(self):
        if self.tie == True:
            print("Tie game!")

        elif self.winner == "X":
            print(f"{self.winner} wins the game!")

        elif self.winner == "O":
            print(f"{self.winner} wins the game!")

        else:
            print(f"It's player {self.turn}'s turn!")

    def switch_turn(self):
        if self.turn == "X":
            self.turn = "O"
            print(f"It's player {self.turn}'s turn!")
        else:
            self.turn = "X"
            print(f"It's player {self.turn}'s turn!")

    def check_for_winner(self):
        # I did all possibilities manualy ..
        if self.board["a1"] and (
            self.board["a1"] == self.board["b1"] == self.board["c1"]
        ):
            print(f"{self.turn} Wins")
            self.turn = "w"
        elif self.board["a1"] and (
            self.board["a1"] == self.board["a2"] == self.board["a3"]
        ):
            print(f"{self.turn} Wins")
            self.turn = "w"

        elif self.board["a1"] and (
            self.board["a1"] == self.board["b2"] == self.board["c3"]
        ):
            print(f"{self.turn} Wins")
            self.turn = "w"
        elif self.board["c1"] and (
            self.board["c1"] == self.board["b2"] == self.board["a3"]
        ):
            print(f"{self.turn} Wins")
            self.turn = "w"

        elif self.board["a2"] and (
            self.board["a2"] == self.board["b2"] == self.board["c2"]
        ):
            print(f"{self.turn} Wins")
            self.turn = "w"
        elif self.board["a3"] and (
            self.board["a3"] == self.board["b3"] == self.board["c3"]
        ):
            print(f"{self.turn} Wins")
            self.turn = "w"

        elif self.board["b1"] and (
            self.board["b1"] == self.board["b2"] == self.board["b3"]
        ):
            print(f"{self.turn} Wins")
            self.turn = "w"
        elif self.board["c1"] and (
            self.board["c1"] == self.board["c2"] == self.board["c3"]
        ):
            print(f"{self.turn} Wins")
            self.turn = "w"

    def check_for_tie(self):
        if (
            self.board["a1"]
            and self.board["a2"]
            and self.board["a3"]
            and self.board["b1"]
            and self.board["b2"]
            and self.board["b3"]
            and self.board["c1"]
            and self.board["c2"]
            and self.board["c3"] != None
            and self.winner == None
        ):
            print("Game Tie")
            self.turn = "t"

    def render(self):
        game_instance.play_game()
        game_instance.print_board()
        game_instance.print_message()
        game_instance.get_move()

    def get_move(self):
        while True:
            move = input(f"Enter a valid movie (example: A1): ").lower()

            if move in ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"):
                if self.board[move] == None:
                    self.board[move] = self.turn
                    game_instance.print_board()
                    game_instance.check_for_winner()
                    game_instance.check_for_tie()
                    if self.turn == "w" or self.turn == "t":
                        break
                    else:
                        game_instance.switch_turn()
                        continue

                else:
                    print("Already Choosen.. Enter another")
                    continue

            else:
                print("Not valid input")
                continue


game_instance = Game("X", False, None, None)
game_instance.render()
