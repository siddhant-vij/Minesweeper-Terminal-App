# [Minesweeper](https://en.wikipedia.org/wiki/Minesweeper) - Python Terminal Game

Minesweeper is a classic single-player puzzle game that originated in the 1960s. The game is played on a grid of squares where some number of squares contain mines. The goal of the game is to uncover all squares without mines.

The player can reveal a square, and if that square doesn't contain a mine, it will show a number indicating how many adjacent squares contain mines. If a square is revealed that contains a mine, the game ends in loss. A square can be flagged by the player to denote that the player believes a mine is present there. The game is won when all non-mine squares are revealed and all mine squares are flagged.

<br>

1. Here are the user stories for the terminal version of Minesweeper Game - MVP:

    - <b> Game Initialization </b>:
        - As a player, I want to be able to start a new game so that I can play Minesweeper.
        - As a player, I want to be able to choose the difficulty level (grid size and number of mines) so that I can control the game's complexity.

    <br>

    - <b> Gameplay </b>:
        - As a player, I want to be able to reveal a square so that I can progress in the game.
        - As a player, I want to see the number of adjacent mines when I reveal a square so that I can make an educated guess on where the mines are located.
        - As a player, I want to be able to flag a square that I think contains a mine so that I can avoid revealing it.
        - As a player, if I reveal a square with a mine, I want the game to end so that I know I've lost.
        - As a player, I want the ability to unflag a square if I believe I made a mistake.

    <br> 

    - <b> Winning/Losing </b>:
        - As a player, I want to know when I've revealed all non-mine squares so that I know I've won.
        - As a player, I want to be able to see where all the mines were located after the game ends so that I can understand where I went wrong in the case of a loss, or see the locations of the mines in a win.

    <br> 

    - <b> UI/UX </b>:
        - As a player, I want a clear and easy-to-understand display of the game grid so that I can see the game state at all times.
        - As a player, I want clear instructions on how to reveal or flag a square so that I can interact with the game properly.
        - As a player, I want clear feedback from the game when I perform an action (like revealing or flagging a square) so that I can understand what is happening in the game.

    <br> 

    - <b> Miscellaneous </b>:
        - As a player, I want the ability to quit the game at any time so that I can stop playing when I want.
        - As a player, I want the game to be fair and random every time I play, so the mines are not in the same location every game.
        - As a player, I want the option to restart a game, so I can start over if I think I've made too many errors.

<br>

2. Here are the user stories for the terminal version of Minesweeper Game - v1:

    - <b> Account Creation and Login </b>:
        - As a player, I want to be able to create an account with a username and password so that I can have a personalized experience.
        - As a player, I want to be able to log in to my account using my username and password so that I can track my progress and continue playing.
        - As a player, I want the system to store my password securely (using hashing) to protect my personal data.

    <br>

    - <b> Game History and Progress Tracking </b>:
        - As a player, I want my game results (win or lose, time taken) to be recorded in the excel database against my account after each game so that I can track my performance over time.
        - As a player, I want to be able to fetch and display my game history (number of games played, won, lost, and best times) from the excel database so that I can understand how I'm improving.

    <br> 

    - <b> Leaderboards </b>:
        - As a player, I want to see the best times and number of wins of top 5 players stored in the excel database so that I can aim to improve my performance.
        - As a player, I want to see my rank based on the number of wins and best times when the leaderboard is displayed, so I can understand where I stand among all players.

    <br> 

    - <b> Advanced Gameplay </b>:
        - As a player, I want a timer displayed in the terminal to track how long I've been playing a game, so that I can challenge myself to complete games faster.
        - As a player, I would like the game to automatically reveal all adjacent squares when I reveal a square that isn't adjacent to any mines, to streamline gameplay.
        - As a player, I want an option to question mark a square that I am unsure about, so that I can come back to it later.
        - As a player, I want to be able to replay the same board after losing, so that I can improve my strategy.

    <br> 

    - <b> Custom Gameplay </b>:
        - As a player, I want to define custom game settings like grid size and number of mines to adjust the difficulty level as per my preference.
        - As a player, I want special types of mines that have different effects when revealed, to add more variety to the game. While replaying, all the special types of mines are replaced with normal mines and now, every mine is a normal mine.
            - Normal Mines: If a normal mine is revealed, the game ends - that's the normal impact of a mine so far.
            - Special Mines: If a special mine is revealed, all non-mine cells are revealed, effectively ending the game.
            - Dud Mines: When revealed, these mines don't end the game as normal mines do. Instead, they can be safely cleared without any consequence.

    <br>

    - <b> Miscellaneous </b>:
        - As a player, I want the game to have multiple lives so that I have a chance to correct my mistakes.

<br>

Note: This is a simple starting point. This implementation covers all the user stories provided above, but it's basic. It uses a an object-oriented approach which makes the code easier to manage and extend. Note that this could be further enhanced with more advanced features, better organization, and better error handling. Here are a certain additions that can be implemented:
- Introducing a time limit for each user input
- Improved gameplay functionality like multiplayer, hints, power-ups or tools
- GUI Implementation
- User profiles & web app functionality
- Backend development
- Unit tests for the functionalities