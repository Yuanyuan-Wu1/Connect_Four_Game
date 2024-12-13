from board import Board
from disk import Disk


def test_init():
    cell_size = 100
    row = 6
    col = 7
    board = Board(cell_size, row, col)
    test_grid = [[None for i in range(col)]
                 for j in range(row)]
    test_Disk = Disk(col, row, 'RED', cell_size/2)
    assert board.cell_size == cell_size and \
        board.width == col and \
        board.height == row and \
        board.grid == test_grid and \
        board.disk == test_Disk and \
        board.current_color == "RED" and \
        not board.disk_dropping


def test_clean_board():
    cell_size = 100
    row = 6
    col = 7
    board = Board(cell_size, row, col)
    test_Disk = Disk(col, row, 'RED', cell_size/2)
    for i in range(row):
        for j in range(col):
            board.grid[i][j] = test_Disk
    board.clean_board()
    for i in range(row):
        for j in range(col):
            assert not board.grid[i][j]


def test_target_position():
    cell_size = 100
    row = 6
    col = 7
    board = Board(cell_size, row, col)
    test_Disk = Disk(col, row, 'RED', cell_size/2)
    board.grid[5][3] = test_Disk
    assert board.target_position(0) == 5
    assert board.target_position(3) == 4
