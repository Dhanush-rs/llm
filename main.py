from snake_ladder import SnakeLadder

def main():

    snakes_input = [
        (14, 7),
        (17, 4),
        (99, 78),
    ]
    ladders_input = [
        (3, 22),
        (5, 8),
        (11, 26),
    ]
    players_input = ["RS", "NS", "SHETTY"]

    # Initialize the game
    game = SnakeLadder(board_size=100, snakes=snakes_input, ladders=ladders_input, players=players_input)

    # Start the game
    game.play_game()
    

if __name__ == "__main__":
    main()