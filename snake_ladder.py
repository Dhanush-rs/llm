from board import Board
from player import Player
import random

class SnakeLadder:
    
    def __init__(self, board_size, snakes, ladders, players):
       self.board = Board(board_size, snakes, ladders)
       self.players = [Player(person) for person in players]
       self.winner = None

    def roll_dice(self):
        return random.randint(1,6)

    def move_player(self, player:Player):
        if self.winner:
            return
        
        position = self.roll_dice()
        initial_position = player.position
        final_position = position + initial_position
        
        if final_position>self.board.board_size:
            final_position=initial_position
    
        final_position = self.board.check_snakes_or_ladders(final_position)
        
        player.position = final_position
        print(f"{player.name} rolled a {position} and moved from {initial_position} to {final_position}")
        if final_position == self.board.board_size:
            self.winner=player.name
            print(f"{player.name} wins the game")
        
    def play_game(self):
        while not self.winner:
            for player in self.players:
                self.move_player(player)
                if self.winner:
                    break


























# import random


# def check_valid_snakes(snakes:list):
#     for k,v in snakes.items():
#         if not (0<= k <=100) or not (0<= v <=100):
#             print("invalid range")
#             return False
#         elif k<v:
#             print("tail should be below head")
#             return False
#         elif k==100:
#             print("can not be at winning position")
#             return False
#         elif (k,v) in ladders.items():
#             print("same head tail for ladder and snake invalid")
#             return False
        
#     return True

# def check_valid_ladders(ladders:list):
    
#     for k,v in ladders.items():
#         if not (0<= k <=100) or not (0<= v <=100):
#             print("invalid range")
#             return False
#         if k>v:
#             print("inverse ladders error")
#             return False
#     return True

# input_snakes = int(input())
# snakes = {}

# for i in range(input_snakes):
#     key, value = map(int,input().split())
#     snakes[key]=value
# print(snakes)

# ladders_count = int(input())
# ladders = {}

# for l in range(ladders_count):
#     key,value =  map(int,input().split())
#     ladders[key] = value
# print(ladders)

# total_players = int(input())
# players = []
# for p in range(total_players):
#     players.append(input())
    
# is_valid_ladders = check_valid_ladders(ladders=ladders)
# is_valid_snakes = check_valid_snakes(snakes=snakes)

# players_position = {}
# for p in players:
#     players_position[p]=0

# Winner=False

# def roll_dice_and_update(players:str):
#     for p in players:
#         dice_roll = random.randint(1,6)
#         while dice_roll%6==0:
#             dice_roll+=random.randint(1,6)
#             if dice_roll==18:
#                 dice_roll=0
#         position=players_position[p]+dice_roll
#         if position==100:
#             print("{} won the game".format(p))
#             return True
#         elif position>100:
#             continue
#         elif position in snakes.keys():
#             players_position[p]=snakes[position]
#         elif position in ladders.keys():
#             players_position[p]=ladders[position]
#         else:
#             players_position[p]=position
        
#         print("{} rolled a {} and moved to {}".format(p, dice_roll, players_position[p]))
#     return False

# if is_valid_ladders and is_valid_snakes:
#     while not Winner:
#         Winner = roll_dice_and_update(players=players)

        
        