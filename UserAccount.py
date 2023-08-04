import os
import pandas as pd
import hashlib
from getpass import getpass

class UserAccount:
    def __init__(self, username):
        self.username = username

    @staticmethod
    def create_account():
        username = input("Enter a username: ")
        password = getpass("Enter a password: ")
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        account_data = pd.DataFrame({
            'Username': [username],
            'PasswordHash': [password_hash]
        })

        if not os.path.exists('user_accounts.xlsx'):
            account_data.to_excel('user_accounts.xlsx', index=False)
        else:
            df = pd.read_excel('user_accounts.xlsx')
            if df[df['Username'] == username].empty:
                df = pd.concat([df, account_data], ignore_index=True)
                df.to_excel('user_accounts.xlsx', index=False)
            else:
                print("Username already exists. Please choose a different username.")

    @staticmethod
    def login():
        attempts = 0
        while attempts < 2:
            username = input("Enter your username: ")

            if not os.path.exists('user_accounts.xlsx'):
                print("No accounts exist. Please create an account first.")
                return None

            df = pd.read_excel('user_accounts.xlsx')

            if df[df['Username'] == username].empty:
                print("Invalid username.")
                return None

            password = getpass("Enter your password: ")
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            if df[(df['Username'] == username) & (df['PasswordHash'] == password_hash)].empty:
                attempts += 1
                if attempts == 2:
                    print("Invalid username or password. You have reached the maximum number of attempts.")
                    return None
                else:
                    print("Invalid password. Please try again.")
            else:
                print("Login successful!")
                return UserAccount(username)


    @staticmethod
    def reset_password(self):
        username = input("Enter your username: ")
        if not os.path.exists('user_accounts.xlsx'):
            print("No accounts exist. Please create an account first.")
            return

        df = pd.read_excel('user_accounts.xlsx')

        if df[df['Username'] == username].empty:
            print("Invalid username.")
            return

        password = getpass("Enter your new password: ")
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        df.loc[df['Username'] == username, 'PasswordHash'] = password_hash
        df.to_excel('user_accounts.xlsx', index=False)

    def record_game_result(self, result, time_taken):
        game_data = pd.DataFrame({
            'Username': [self.username],
            'Result': [result],
            'TimeTaken': [int(time_taken)]
        })

        if not os.path.exists('games.xlsx'):
            game_data.to_excel('games.xlsx', index=False)
        else:
            df = pd.read_excel('games.xlsx')
            df = pd.concat([df, game_data], ignore_index=True)
            df.to_excel('games.xlsx', index=False)

    def get_game_history(self):
        if not os.path.exists('games.xlsx'):
            print("No game history exists.")
            return
        df = pd.read_excel('games.xlsx')
        user_games = df[df['Username'] == self.username]
        if user_games.empty:
            print("You have not played any games yet.")
        else:
            print("Your game history:")
            user_games.index = user_games.index + 1  # adjust index to be 1-based
            print(user_games)

    def get_leaderboard_position(self):
        if not os.path.exists('games.xlsx'):
            print("No game data exists.")
            return
        df = pd.read_excel('games.xlsx')
        won_games = df[df['Result'] == 'win']
        leaderboard = won_games.groupby('Username').agg({'Result': 'count', 'TimeTaken': 'min'}).rename(columns={'Result': 'Wins', 'TimeTaken': 'BestTime'}).sort_values(by=['Wins', 'BestTime'], ascending=[False, True])
        if leaderboard.empty:
            print("No games have been won yet.")
        else:
            print("Leaderboard:")
            print(leaderboard.head(5))
            user_rank = leaderboard.reset_index().index[leaderboard.reset_index()['Username'] == self.username].tolist()
            if user_rank:
                print(f"Your rank: {user_rank[0] + 1}")
            else:
                print("You have not won any games yet.")
