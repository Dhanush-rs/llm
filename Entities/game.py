from Entities.board import Board
from Entities.players import Players

class Game:
    values = ["X","O"]
    def __init__(self, size, players):
        self.board= Board(3)
        self.board.set_board()
        self.players= []
        for player,value in players,self.values:
            player_obj = Players(name=player)
            player_obj.set_value(value)
            self.players.append(player_obj)
            
    def update_board(self, player, value, position):
        if value != player.value:
            print("invalid operation")
            return False
        self.board.update_board(value, position)
    
    def play(self):
        pass
            
        
        
            