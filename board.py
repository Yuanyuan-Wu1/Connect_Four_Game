from disk import Disk
import numpy as np


class Board:

    def __init__(self, cell_size, height, width):
        """inition the board"""
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.grid = [[None for i in range(self.width)]
                     for j in range(self.height)]
        self.heights = [0] * self.width
        self.disk_dropping = False
        self.disk = Disk(width, height, 'RED', cell_size/2)
        self.current_color = "RED"

    def draw_board(self):
        """绘制棋盘"""
        self.display_disk()
        
        # 设置线条样式
        pushStyle()  # 保存当前样式
        strokeWeight(20)
        stroke(0, 0, 255)
        
        # 绘制垂直线
        for i in range(self.width + 1):
            x = i * self.cell_size
            y1 = self.cell_size
            y2 = (self.height + 1) * self.cell_size
            line(x, y1, x, y2)

        # 绘制水平线
        for j in range(self.height + 1):
            y = self.cell_size + j * self.cell_size
            x1 = 0
            x2 = self.width * self.cell_size
            line(x1, y, x2, y)
        
        popStyle()  # 恢复之前的样式

    def clean_board(self):
        """clean board for a new game"""
        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j] = None
        self.display_disk()

    def display_disk(self):
        """display disk"""
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j]:
                    self.grid[i][j].draw_disk()

    def target_position(self, colum):
        """look for the position"""
        for heightRun in range(self.height-1, -1, -1):
            if self.grid[heightRun][colum] is None:
                return heightRun
        return None

    def add_disk(self, colum):
        """add the disk, when game over print game over"""
        row = self.target_position(colum)
        if row is not None and colum is not None:
            new_disk = Disk(colum, row, self.current_color, 50)
            self.grid[row][colum] = new_disk
            new_disk.drop_disk(row)
        if self.current_color == "YELLOW":
            self.current_color = "RED"
        else:
            self.current_color = "YELLOW"
