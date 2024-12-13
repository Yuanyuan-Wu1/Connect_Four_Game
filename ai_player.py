import random
import time

from board import Board
from disk import Disk

CELL = 100


class ai_player:
    def __init__(self, board, disk):
        self.board = board
        self.disk = disk

    def get_valid_column(self):
        # check if game over

        # get a valid column to play if the game is not over
        col = random.randint(0, self.board.width-1)
        while(self.board.grid[0][col] == 0):
            col = random.randint(0, self.board.width-1)
        return col
    
    def play(self):
        time.sleep(2)
        col = self.get_valid_column()
        self.disk.drop_disk(col)

    def evaluate_position(self, board):
        score = 0
        
        # 水平方向评估
        for row in range(6):
            for col in range(4):
                window = board[row][col:col+4]
                score += self.evaluate_window(window)
        
        # 垂直方向评估
        for row in range(3):
            for col in range(7):
                window = [board[row+i][col] for i in range(4)]
                score += self.evaluate_window(window)
                
        # 对角线方向评估
        # ... 类似逻辑
        
        return score

    def evaluate_window(self, window):
        score = 0
        ai_pieces = window.count(2)  # AI棋子
        human_pieces = window.count(1)  # 人类棋子
        empty = window.count(0)  # 空位
        
        if ai_pieces == 4:
            score += 100
        elif ai_pieces == 3 and empty == 1:
            score += 5
        elif ai_pieces == 2 and empty == 2:
            score += 2
            
        if human_pieces == 3 and empty == 1:
            score -= 4
            
        return score
