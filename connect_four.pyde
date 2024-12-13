import random
import time
import logging

from board import Board
from disk import Disk
from game_controller import GameController

SPACE = {'width': 700, 'height': 700}
target_y = 50
cell_size = 100
row = 6
col = 7
board = Board(cell_size, row, col)
gc = GameController(board)
MOUSE_AREA = 100
ai_thinking_time = 500

def setup():
    """
    a function to set up the background
    """
    size(SPACE['width'], SPACE['height'])
    width = SPACE['width']
    height = SPACE['height']
    colorMode(RGB, 1)
    board.draw_board()
    ask_input()

def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

def ask_input():
    answer = input('enter your name')
    if answer:
        print('hi ' + answer)
        gc.player_list[answer] = 0
        gc.cur_human_player_name = answer
    elif answer == '':
        print('[empty string]')
    else:
        print(answer) # Canceled dialog will print None

def draw():
    """
    a function to draw disk at the point of mouse click
    """    
    background(0.8)
    board.draw_board()
    if(gc.is_game_over):
        gc.print_game_over()
    ai_player_play()

def ai_player_play():
    if gc.current_player == -1 and not gc.is_game_over:
        try:
            # 获取AI移动
            col = gc.get_ai_move()
            if col is not None:
                delay(ai_thinking_time)
                board.add_disk(col)
                gc.check_board_full()
                gc.check_winner()
                gc.switch_player()
            else:
                logging.warning("AI couldn't find a valid move")
        except Exception as e:
            logging.error(f"Error during AI move: {e}")

def mouseReleased():
    if(gc.current_player == 1 and not gc.is_game_over):
        board.add_disk(mouseX // cell_size)
        gc.check_board_full()
        gc.check_winner()
        gc.switch_player()
        return
    if(gc.is_game_over):
        gc.start_new_game()
        gc.check_winner()
        
