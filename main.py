from Entities.board import Board
from Entities.game import Game
def main():
    players = ["RS","NS"]
    game =  Game(3,players)
    game.board.set_board()  
    game.board.get_board()  

if __name__ == "__main__":
    main()