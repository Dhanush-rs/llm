
class Board:
    
    def __init__(self, board_size, snakes, ladders):
        self.board_size = board_size
        self.snakes = {head:tail for head,tail in snakes}
        self.ladders = {start:end for start, end in ladders}
        
    def check_snakes_or_ladders(self,position):
        
        while position in self.snakes or position in self.ladders:
            if position in self.snakes:
                position=self.snakes[position]
            elif position in self.ladders:
                position = self.ladders[position]
        
        return position