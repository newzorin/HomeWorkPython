import random
import os
from random import choice, randint

def start_game():
    print("Привет это игра про конфеты вот правила")
    print("На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. \
        \nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. \
        \nВсе конфеты оппонента достаются сделавшему последний ход.")
    print()
    print("Определяем очередность ходов:")
    chance = random.randint(0, 1)
    if chance == 0:
        print("Сегодня твой день, первый ход за тобой")
        return True
    else:
        print("Не повезло тебе приятель, сегодня ты ходишь вторым")
        return False
def player_turn():
    print("Введите количество конфет которое вы хотите взять (не более 28)")
    turn = 100
    while turn > 28:
        turn = int(input())
    print("Ты взял", turn, "конфет")
    return turn
def ai_turn():
    turn = 2023
    while turn > candies:        
        turn = candies % 29 if not candies % 29 else randint(1,28)
    print("бот взял", turn, "конфет")
    return turn

def print_candies():
    print("Количество оставшихся конфет:", candies)
    print("")
    return

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    if start_game():
        player_first = True
    else:
        player_first = False
    global candies
    candies = 202
   
    win = ""

    
    while candies > 1:

        if player_first:
            candies -= player_turn()
            if candies <= 0:
                win = "Игрок"
                break
            print_candies()
            candies -= ai_turn()
            if candies <= 0:
                win = "бот"
                break
            print_candies()
        else:
            candies -= ai_turn()
            if candies <= 0:
                win = "бот"
                break
            print_candies()
            candies -= player_turn()
            if candies <= 0:
                win = "Игрок"
                break
            print_candies()
    print("Выиграл", win)
        

if __name__ == "__main__":
    main()
