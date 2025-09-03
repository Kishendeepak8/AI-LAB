
from collections import deque

N = 3

class PuzzleState:
    def __init__(self, board, x, y, depth):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth

row = [0, 0, -1, 1]
col = [-1, 1, 0, 0]

def is_goal_state(board):
    goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    return board == goal

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))
    print("--------")

def solve_puzzle_idfs(start, x, y):
    def dfs(curr_state, limit, visited):
       
        if curr_state.depth > limit:
            return False
        
        print(f'Depth: {curr_state.depth}')
        print_board(curr_state.board)

        if is_goal_state(curr_state.board):
            print(f'Goal state reached at depth {curr_state.depth}')
            return True

        for i in range(4):
            new_x = curr_state.x + row[i]
            new_y = curr_state.y + col[i]

            if is_valid(new_x, new_y):
                new_board = [row[:] for row in curr_state.board]
                
                new_board[curr_state.x][curr_state.y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[curr_state.x][curr_state.y]

                board_tuple = tuple(map(tuple, new_board))
                if board_tuple not in visited:
                    visited.add(board_tuple)
                    next_state = PuzzleState(new_board, new_x, new_y, curr_state.depth + 1)
                    
                    if dfs(next_state, limit, visited):
                        return True

        return False

    depth_limit = 0
    while True:
        visited = set()
        visited.add(tuple(map(tuple, start)))
        
        print(f"Trying with depth limit: {depth_limit}")
        
        if dfs(PuzzleState(start, x, y, 0), depth_limit, visited):
            break
        
        depth_limit += 1  

    print('Solution found.')

if __name__ == '__main__':
    start = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
    x, y = 1, 1

    print('Initial State:')
    print_board(start)

    solve_puzzle_idfs(start, x, y)

