import pytest
from src.problem10 import game_of_life


class TestGameOfLife:
    def test_example_1(self):
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        game_of_life(board)
        assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

    def test_example_2(self):
        board = [[1, 1], [1, 0]]
        game_of_life(board)
        assert board == [[1, 1], [1, 1]]

    def test_all_dead(self):
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        game_of_life(board)
        assert board == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def test_single_cell_dies(self):
        """A single live cell has no neighbors -> dies."""
        board = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        game_of_life(board)
        assert board == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def test_block_stable(self):
        """A 2x2 block is a 'still life' - it never changes."""
        board = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
        game_of_life(board)
        assert board == [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]

    def test_blinker_oscillator(self):
        """Horizontal blinker becomes vertical."""
        board = [[0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0]]
        game_of_life(board)
        assert board == [[0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 1, 1, 1, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0]]

    def test_blinker_period_2(self):
        """Applying blinker twice returns to original state."""
        board = [[0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0]]
        game_of_life(board)
        game_of_life(board)
        assert board == [[0, 0, 0, 0, 0],
                         [0, 0, 1, 0, 0],
                         [0, 0, 1, 0, 0],
                         [0, 0, 1, 0, 0],
                         [0, 0, 0, 0, 0]]

    def test_underpopulation(self):
        """Live cell with 1 neighbor dies."""
        board = [[1, 1, 0], [0, 0, 0], [0, 0, 0]]
        game_of_life(board)
        assert board == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def test_overpopulation(self):
        """Live cell with 4+ neighbors dies."""
        board = [[1, 1, 1], [1, 1, 0], [0, 0, 0]]
        game_of_life(board)
        # center cell (1,1) has 4 live neighbors -> dies
        # corners and edges recalculated accordingly
        assert board[1][1] == 0

    def test_reproduction(self):
        """Dead cell with exactly 3 neighbors becomes alive."""
        board = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
        game_of_life(board)
        # center stays alive (2 neighbors), left/right of center come alive (3 neighbors)
        assert board[1][0] == 1
        assert board[1][1] == 1
        assert board[1][2] == 1

    def test_returns_none(self):
        """Function modifies in-place, returns None."""
        board = [[1, 0], [0, 1]]
        result = game_of_life(board)
        assert result is None

    def test_1x1_grid(self):
        board = [[1]]
        game_of_life(board)
        assert board == [[0]]

    def test_1x1_dead(self):
        board = [[0]]
        game_of_life(board)
        assert board == [[0]]
