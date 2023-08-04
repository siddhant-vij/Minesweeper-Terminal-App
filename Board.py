from Cell import Cell
import numpy as np
import random

class Board:
    def __init__(self, rows, cols, num_mines, mine_locations=None):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.mine_locations = mine_locations
        self.is_game_over = False
        self.is_game_won = False
        self.lives = 3  # Set default lives to 3
        self.cells = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self.place_mines()

    def get_mine_locations(self):
        return [(cell.row, cell.col, cell.mine_type) for cell in self.cells if cell.is_mine]
        
    def place_mines(self):
        mine_types = ['normal', 'special', 'dud']
        probabilities = [0.7, 0.15, 0.15]

        if self.mine_locations is None:
            mine_indices = np.random.choice(self.rows * self.cols, self.num_mines, replace=False)
            self.mine_locations = [(index // self.cols, index % self.cols) for index in mine_indices]
            for (x, y) in self.mine_locations:
                self.cells[x][y].mine_type = random.choices(mine_types, probabilities)[0]

        for (x, y) in self.mine_locations:
            self.cells[x][y].is_mine = True

        for row in range(self.rows):
            for col in range(self.cols):
                if self.cells[row][col].is_mine:
                    continue
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if dr == 0 and dc == 0:
                            continue
                        new_row, new_col = row + dr, col + dc
                        if new_row < 0 or new_row >= self.rows or new_col < 0 or new_col >= self.cols:
                            continue
                        if self.cells[new_row][new_col].is_mine:
                            self.cells[row][col].adjacent_mines += 1
                    

    def print_board(self):
        print(f"Remaining lives: {self.lives}")
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cells[row][col]
                if cell.is_revealed:
                    if cell.is_mine:
                        if cell.mine_type == 'special':
                            print('S', end=' ')
                        elif cell.mine_type == 'dud':
                            print('D', end=' ')
                        else:
                            print('M', end=' ')
                    else:
                        print(cell.adjacent_mines, end=' ')
                elif cell.is_flagged:
                    print('F', end=' ')
                elif cell.is_question_marked:
                    print('?', end=' ')
                else:
                    print('X', end=' ')
            print()

    def question_mark(self, row, col):
        cell = self.cells[row][col]
        if cell.is_revealed:
            print("The cell is already revealed and can't be question marked.")
            return False
        elif cell.is_flagged:
            print("The cell is flagged and can't be question marked.")
            return False
        else:
            cell.is_question_marked = not cell.is_question_marked
            return True
    
    def reveal(self, row, col):
        cell = self.cells[row][col]
        if cell.is_flagged:
            print("The cell is flagged and can't be revealed.")
            return False
        elif cell.is_question_marked:
            print("The cell is question marked and can't be revealed.")
            return False
        elif cell.is_revealed:
            print("The cell is already revealed.")
            return False
        cell.is_revealed = True
        if cell.is_mine:
            if cell.mine_type == 'special':
                print("You hit a special mine! All non-mine cells are revealed.")
                self.reveal_all_non_mines()
                self.check_game_won()
            elif cell.mine_type == 'dud':
                return None
            else:  # normal mine
                print("You hit a normal mine!")
                self.lives -= 1  # Decrement lives when a mine is revealed
                if self.lives == 0:
                    self.is_game_over = True
        elif cell.adjacent_mines == 0:
            self.reveal_adjacent(row, col)
        return True

    def reveal_all_non_mines(self):
        for row in self.cells:
            for cell in row:
                if not cell.is_mine:
                    cell.is_revealed = True

    def reveal_adjacent(self, row, col):
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                new_row, new_col = row + dr, col + dc
                if new_row < 0 or new_row >= self.rows or new_col < 0 or new_col >= self.cols:
                    continue
                if not self.cells[new_row][new_col].is_revealed and not self.cells[new_row][new_col].is_mine:
                    self.cells[new_row][new_col].is_revealed = True
                    if self.cells[new_row][new_col].adjacent_mines == 0:
                        self.reveal_adjacent(new_row, new_col)


    def flag(self, row, col):
        cell = self.cells[row][col]
        if cell.is_revealed:
            print("The cell is already revealed and can't be flagged.")
            return False
        elif cell.is_question_marked:
            print("The cell is question marked and can't be flagged.")
            return False
        else:
            cell.is_flagged = not cell.is_flagged
            return True

    def check_game_won(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.cells[row][col].is_revealed and not self.cells[row][col].is_mine:
                    return
        self.is_game_won = True

    def reveal_mines(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.cells[row][col].is_mine:
                    self.cells[row][col].is_revealed = True
        self.print_board()
