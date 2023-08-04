import sys
from Board import Board
from UserAccount import UserAccount
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')    

def play_game(account, last_difficulty=None, last_mine_locations=None, is_replay=False):
    # Difficulty levels
    difficulty_levels = {
        '1': (5, 5),  # easy
        '2': (10, 10),  # medium
        '3': (15, 15)  # hard
    }
    if not is_replay:
        # Game start option
        while True:
            print("\n\nEnter 'start' to start a new game")
            print("Enter 'history' to view your game history")
            print("Enter 'leaderboard' to view the leaderboard")
            print("Enter 'reset' to reset password")
            print("Enter 'quit' to quit")
            action = input("\nChoose an option: ")
            clear_screen()
            if action.lower() == 'start':
                print("Starting a new game of Minesweeper.\nEnter 'quit' to exit the game or 'restart' to start a new game at any time.")
                break
            elif action.lower() == 'history':
                account.get_game_history()
            elif action.lower() == 'leaderboard':
                account.get_leaderboard_position()
            elif action.lower() == 'reset':
                UserAccount.reset_password()
            elif action.lower() == 'quit':
                print("Exiting the game...")
                return
            else:
                print("Invalid action. Please enter 'start', 'history', 'leaderboard', 'reset', or 'quit'.")

        # Choose difficulty level
        difficulty = input("Choose difficulty level:\n1 - Easy\n2 - Medium\n3 - Hard\n4 - Custom\n")
        if difficulty.lower() == 'quit':
            print("Exiting the game...")
            return
        if difficulty not in ['1', '2', '3', '4']:
            print("Invalid difficulty level. Defaulting to Easy.")
            difficulty = '1'
    else:
        difficulty = last_difficulty
    
    if difficulty == '4':  # Custom difficulty
        while True:
            try:
                board_size = int(input("Enter grid size: "))
                num_mines = int(input("Enter number of mines: "))
                if board_size < 1 or num_mines < 1 or num_mines >= board_size ** 2:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Grid size and number of mines must be positive integers, and the number of mines must be less than the total number of cells in the grid.")
    else:
        difficulty_levels = {
            '1': (5, 5),  # easy
            '2': (10, 10),  # medium
            '3': (15, 15)  # hard
        }
        board_size, num_mines = difficulty_levels[difficulty]

    # Create a new board
    board = Board(board_size, board_size, num_mines, last_mine_locations)

    start_game = input("\n\n\nWould you like to start the game? (yes/no): ")
    if start_game.lower() != 'yes':
        print("Exiting the game...")
        return
    
    start_time = time.time()  # Start the timer

    # Game loop
    while True:
        clear_screen()
        board.print_board()
        elapsed_time = time.time() - start_time
        print(f'Elapsed time: {int(elapsed_time)} seconds')
        while True:
            action = input("Enter 'r' to reveal a cell, 'f' to flag a cell, 'q' to question mark a cell: ")
            if action.lower() == 'quit':
                print("Exiting the game...")
                board.reveal_mines()
                return
            if action.lower() == 'restart':
                print("Starting a new game...")
                board.reset()
                board.place_mines()
                break
            if action not in ['r', 'f', 'q']:
                print("Invalid action. Enter 'r' 'f' or 'q' proceed further.")
                continue
            try:
                x, y = map(int, input("Enter the coordinates of the cell (x, y): ").split())
                # Convert to 0-based indexing
                x, y = x - 1, y - 1
                if action.lower() == 'r':
                    result = board.reveal(x, y)
                    if result:
                        break
                    elif result is None:
                        print("You hit a dud mine! No harm done.")
                        start_game = input("\n\n\nWould you like to continue the game? (yes/no): ")
                        if start_game.lower() != 'yes':
                            print("Exiting the game...")
                            return
                        else:
                            break
                if action.lower() == 'f':
                    if board.flag(x, y):
                        break
                if action.lower() == 'q':
                    if board.question_mark(x, y):
                        break
            except ValueError:
                print("Invalid cell coordinates. Please enter two numbers separated by a space.")
            except IndexError:
                print("Cell coordinates are out of the board range. Please reenter.")
        if board.is_game_over:
            end_time = time.time()  # End the timer
            total_time = end_time - start_time
            print(f'Game Over! You revealed a mine. Total time: {int(total_time)} seconds')
            board.reveal_mines()
            account.record_game_result('lose', end_time - start_time)
            
            replay = input("Do you want to replay the same board? (yes/no): ")
            if replay == 'yes':
                return play_game(account, last_difficulty=difficulty, last_mine_locations=board.mine_locations, is_replay=True)
            else:
                return # play_game(account)
        board.check_game_won()
        if board.is_game_won:
            end_time = time.time()  # End the timer
            total_time = end_time - start_time
            print(f'Congratulations! You have won the game. Total time: {int(total_time)} seconds')
            board.reveal_mines()
            account.record_game_result('win', end_time - start_time)
            return

if __name__ == "__main__":
    print("Welcome to Minesweeper!")
    # Sign up and Login
    while True:
        action = input("Enter 'login' to log in, 'create' to create an account, 'reset' to reset password, or 'quit' to quit: ")
        clear_screen()
        if action.lower() == 'login':
            account = UserAccount.login()
            if account is not None:
                break
        elif action.lower() == 'create':
            UserAccount.create_account()
        elif action.lower() == 'reset':
            UserAccount.reset_password()
        elif action.lower() == 'quit':
            print("Exiting the game...")
            sys.exit()
        else:
            print("Invalid action. Please enter 'login', 'create', 'reset', or 'quit'.")
    play_game(account)
