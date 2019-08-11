from FootballGame import FootballGame
import os

game = FootballGame()

if __name__ == '__main__':
    print(os.getcwd())
    print("Starting game instance...")
    game.start()
