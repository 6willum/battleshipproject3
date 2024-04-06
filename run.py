class BattleshipGame:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grids = {'Player 1': [[' ' for _ in range(grid_size)] for _ in range(grid_size)],
                      'Player 2': [[' ' for _ in range(grid_size)] for _ in range(grid_size)]}
        self.ships = {'Player 1': [], 'Player 2': []}

    def print_grid(self, player):
        opponent = 'Player 1' if player == 'Player 2' else 'Player 2'
        print(f"{player}'s guesses:")
        header = '  ' + ' '.join([str(i) for i in range(self.grid_size)])
        print(header)
        for r, row in enumerate(self.grids[opponent]):
            print(f"{r} {' '.join(row)}")
        print("\n")

    def place_ship(self, player):
        print(f"{player}, place your 4 ships on the grid.")
        for _ in range(4):  # Allow placement of 4 ships
            valid = False
            while not valid:
                try:
                    location = input("Enter the coordinates to place your ship (row,col): ")
                    row, col = map(int, location.split(','))
                    if (row, col) in self.ships[player] or not (0 <= row < self.grid_size) or not (0 <= col < self.grid_size):
                        print("Invalid location. Try again.")
                    else:
                        valid = True
                        self.ships[player].append((row, col))
                except ValueError:
                    print("Invalid input. Please enter row,col (e.g., 1,2).")

    def make_guess(self, player):
        valid = False
        while not valid:
            try:
                location = input(f"{player}, enter the coordinates to guess (row,col): ")
                row, col = map(int, location.split(','))
                if not (0 <= row < self.grid_size) or not (0 <= col < self.grid_size):
                    print("Guess out of bounds. Try again.")
                else:
                    valid = True
                    opponent = 'Player 1' if player == 'Player 2' else 'Player 2'
                    if (row, col) in self.ships[opponent]:
                        print("Hit!")
                        self.grids[player][row][col] = 'X'
                        self.ships[opponent].remove((row, col))
                        if not self.ships[opponent]:
                            print(f"All ships sunk. {player} wins!")
                            return True
                    else:
                        print("Miss!")
                        self.grids[player][row][col] = 'O'
            except ValueError:
                print("Invalid input. Please enter row,col (e.g., 1,2).")
        return False

    def play(self):
        print("Welcome to Battleship!")
        self.place_ship('Player 1')
        self.place_ship('Player 2')

        turn = 'Player 1'
        while True:
            self.print_grid(turn)
            if self.make_guess(turn):
                break
            turn = 'Player 1' if turn == 'Player 2' else 'Player 2'

if __name__ == "__main__":
    size = input("Enter the grid size (e.g., 5 for a 5x5 grid): ")
    game = BattleshipGame(int(size))
    game.play()
