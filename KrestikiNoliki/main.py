import game
import board
game.set_player_names()
board.draw_board()
while True:
    if game.game_turn():
        break
