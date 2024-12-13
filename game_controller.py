from board import Board
from disk import Disk
from functools import lru_cache
import random
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='game.log'
)

class GameController:

    def __init__(self, board):
        """inition the game controller"""
        try:
            self.my_board = board
            self.is_game_over = False
            self.height = board.height
            self.width = board.width
            self.current_player = 1
            self.drop_count = 0
            self.player_list = {}
            self.ai_name = "AI"
            self.player_list[self.ai_name] = 0
            self.cur_human_player_name = ""
            self.difficulty = "medium"  # easy, medium, hard
            logging.info("Game controller initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing game controller: {e}")
            raise

    def board_full(self):
        """
        A function to check if the board if full
        """
        return self.drop_count == self.height * self.width

    def print_game_over(self):
        """显示游戏结束信息"""
        if self.is_game_over:
            pushStyle()  # 保存当前样式
            
            # 设置文本样式
            strokeWeight(10)
            fill(255, 0, 0)
            textSize(32)
            stroke(0, 0, 0)
            textAlign(CENTER, CENTER)  # 文本居中对齐
            
            # 计算文本位置
            x = (self.width * self.my_board.cell_size) / 2
            y = 60
            
            # 显示获胜信息
            if self.current_player == -1:
                message = f"{self.cur_human_player_name} WINS! Click to start a new game"
            else:
                message = "AI WINS! Click to start a new game"
                
            text(message, x, y)
            
            popStyle()  # 恢复之前的样式

    def start_new_game(self):
        """
        A function to start new game when game over
        """
        self.is_game_over = False
        self.my_board.clean_board()
        self.drop_count = 0
        self.current_player = 1
        self.my_board.current_color = "RED"

    def check_board_full(self):
        """
        A function to check board is full or not
        """
        if(self.drop_count == self.height * self.width):
            self.is_game_over = True
            strokeWeight(10)
            fill(255, 0, 0)
            textSize(32)
            stroke(0, 0, 0)
            text("Board full! no winner, click to restart a new game", 10, 60)

    def record_score(self):
        """记录分数并保存到文件"""
        try:
            # 更新分数
            if self.current_player == -1:
                self.player_list[self.ai_name] += 1
            else:
                self.player_list[self.cur_human_player_name] += 1

            # 写入文件
            with open("scores.txt", "a") as f:
                for player, score in self.player_list.items():
                    f.write(f"{player}: {score}\n")
                
        except IOError as e:
            print(f"Error writing to scores file: {e}")

    def check_winner(self):
        """检查获胜者"""
        self.drop_count += 1
        board = self.my_board
        
        def check_window(window):
            """检查一个窗口是否获胜"""
            if not window[0]:
                return False
            return all(cell and cell.color == window[0].color for cell in window)
        
        # 水平检查
        for row in range(self.height):
            for col in range(self.width - 3):
                window = [board.grid[row][col+i] for i in range(4)]
                if check_window(window):
                    self._handle_win()
                    return True
                
        # 垂直检查
        for row in range(self.height - 3):
            for col in range(self.width):
                window = [board.grid[row+i][col] for i in range(4)]
                if check_window(window):
                    self._handle_win()
                    return True
        
        # 对角线检查 (正斜)
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                window = [board.grid[row+i][col+i] for i in range(4)]
                if check_window(window):
                    self._handle_win()
                    return True
        
        # 对角线检查 (反斜)
        for row in range(3, self.height):
            for col in range(self.width - 3):
                window = [board.grid[row-i][col+i] for i in range(4)]
                if check_window(window):
                    self._handle_win()
                    return True
        
        return False

    def _handle_win(self):
        """处理获胜情况"""
        self.is_game_over = True
        self.print_game_over()
        self.record_score()

    def print_turn(self):
        """print turn"""
        strokeWeight(10)
        fill(255, 255, 255)
        textSize(32)
        stroke(0, 0, 0)
        if(self.current_player == 1):
            text("Human turn:", 10, 60)
            return
        else:
            text("AI turn:", 10, 60)

    def switch_player(self):
        """switch the player"""
        if(self.current_player == 1):
            self.current_player = -1
            strokeWeight(10)
            fill(255, 255, 255)
            textSize(32)
            stroke(0, 0, 0)
            text("AI turn:", 10, 60)
        else:
            self.current_player = 1

    def minimax(self, board, depth, alpha, beta, is_maximizing):
        # 基本情况：检查是否达到终止条件
        if self.is_terminal_node(board) or depth == 0:
            return self.evaluate_position(board)
        
        if is_maximizing:
            max_eval = float('-inf')
            for move in self.get_valid_moves(board):
                evaluation = self.minimax(board, depth-1, alpha, beta, False)
                max_eval = max(max_eval, evaluation)
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.get_valid_moves(board):
                evaluation = self.minimax(board, depth-1, alpha, beta, True)
                min_eval = min(min_eval, evaluation)
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            return min_eval

    @lru_cache(maxsize=1000)
    def get_winning_moves(self, board_state):
        # 将棋盘状态转换为可哈希的元组
        board_tuple = tuple(map(tuple, board_state))
        # 计算获胜移动
        # ...

    def set_ai_difficulty(self, difficulty):
        self.difficulty = difficulty
        
    def get_ai_move(self):
        if self.difficulty == "easy":
            return self.random_move()
        elif self.difficulty == "medium":
            return self.minimax(depth=3)
        else:  # hard
            return self.minimax(depth=5)

    def get_valid_moves(self, board):
        """获取所有可用的移动位置"""
        valid_moves = []
        for col in range(self.width):
            if board.grid[0][col] is None:  # 如果最顶层为空
                valid_moves.append(col)
        return valid_moves

    def is_terminal_node(self, board):
        """检查是否为终止点"""
        # 检查是否有获胜者
        if self.check_winner():
            return True
        # 检查是否平局
        return self.board_full()

    def random_move(self):
        """生成随机移动"""
        valid_moves = self.get_valid_moves(self.my_board)
        if valid_moves:
            return random.choice(valid_moves)
        return None

    def evaluate_position(self, board):
        """评估当前局面"""
        score = 0
        # 水平方向评估
        for row in range(self.height):
            for col in range(self.width - 3):
                window = [board.grid[row][col+i] for i in range(4)]
                score += self._evaluate_window(window)
        
        # 垂直方向评估
        for row in range(self.height - 3):
            for col in range(self.width):
                window = [board.grid[row+i][col] for i in range(4)]
                score += self._evaluate_window(window)
        
        return score

    def _evaluate_window(self, window):
        """评估一个窗口的分数"""
        score = 0
        ai_pieces = sum(1 for piece in window if piece and piece.color == "YELLOW")
        human_pieces = sum(1 for piece in window if piece and piece.color == "RED")
        empty = sum(1 for piece in window if piece is None)
        
        if ai_pieces == 4:
            score += 100
        elif ai_pieces == 3 and empty == 1:
            score += 5
        elif ai_pieces == 2 and empty == 2:
            score += 2
        
        if human_pieces == 3 and empty == 1:
            score -= 4
        
        return score
