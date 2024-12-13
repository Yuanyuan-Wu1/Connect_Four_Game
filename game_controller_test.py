from game_controller import GameController
from board import Board

def test_init():
    """Test for game_controller function"""
    # 创建测试用的board实例
    cell_size = 100
    height = 6
    width = 7
    board = Board(cell_size, height, width)
    
    # 创建GameController实例
    gc = GameController(board)
    
    # 测试初始化值是否正确
    assert gc.my_board == board
    assert gc.is_game_over == False
    assert gc.height == board.height
    assert gc.width == board.width
    assert gc.current_player == 1
    assert gc.drop_count == 0
    assert gc.ai_name == "AI"
    assert gc.player_list[gc.ai_name] == 0
    assert gc.cur_human_player_name == ""