import board as play_board

player_one_name = ""
player_two_name = ""
current_player = player_one_name
mark = "Х"
game_bot_mode = False

def set_player_names():
    global player_one_name
    global player_two_name
    global game_bot_mode
    global current_player
    while player_one_name == "":
        player_one_name = input("Первый игрок:")
        current_player = player_one_name
    player_two_name = input("Второй игрок:"
                            "(Enter для игры против бота):")
                    
    if not player_two_name:
        player_two_name = "ботик"
        game_bot_mode = True

def switch_player():
    global mark
    global player_one_name
    global player_two_name
    global current_player
    if mark == "Х":
        current_player = player_two_name
        mark = "0"
    else:
        current_player = player_one_name
        mark = "Х"

def game_turn():
    global mark
    global player_one_name
    global player_two_name
    global current_player
    switch_player()
    
    position = ""
    if current_player == player_two_name and game_bot_mode:
        position = bot_turn()
    else:
        position = player_turn() 

    play_board.set_board(position, mark)
    board = play_board.get_board()
    play_board.draw_board()
    for pos in play_board.win_con:
        if board[pos[0]] == board[pos[1]] == board[pos[2]]:
            print(f"Побеждает {mark} под управлением {current_player} ")
            return True
    

    

def player_turn():
    global current_player
    while True:
        try:
            position = int(input(f"{current_player} Введите позицию: "))
            if position in play_board.get_board():
                return position
            else:
                print("Эта позиция занята")  
        except ValueError:
            print("Будьте добры выражайтесь цифрами") 
      
def bot_turn():
    pass    