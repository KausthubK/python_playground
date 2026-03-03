"""
Problem 10: Conway's Game of Life (Canva Interview Question)
=============================================================
~12 minutes | NumPy allowed (or pure Python — your choice)

The board is an m x n grid of cells. Each cell is live (1) or dead (0).
Each cell interacts with its 8 neighbors (horizontal, vertical, diagonal).

Rules (applied SIMULTANEOUSLY to all cells):
    1. Live cell with < 2 live neighbors -> dies (under-population)
    2. Live cell with 2 or 3 live neighbors -> lives
    3. Live cell with > 3 live neighbors -> dies (over-population)
    4. Dead cell with exactly 3 live neighbors -> becomes alive (reproduction)

Implement:
    game_of_life(board: list[list[int]]) -> None
    - Modify the board IN-PLACE to reflect the next state
    - Do NOT return anything
    - All updates happen simultaneously (you can't update cells one by one
      and use the new values for other cells in the same generation)

Examples:
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    game_of_life(board)
    # board is now [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

    board = [[1,1],[1,0]]
    game_of_life(board)
    # board is now [[1,1],[1,1]]

Hint: You need a way to record the "original" state while updating.
      Options: copy the board first, or encode state transitions in-place
      using values like 2 (was alive, now dead) and 3 (was dead, now alive).

Constraint: Must update in-place. No external imports required,
            but numpy is available if you want it.
"""


def game_of_life(board: list[list[int]]) -> None:
    raise NotImplementedError
