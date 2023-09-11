from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        rows = len(grid)
        cols = len(grid[0])

        start_row = -1
        start_col = -1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    start_row = row
                    start_col = col
                    break
        first_island_queue = deque()
        first_island_queue.append((start_row, start_col))

        second_island_queue = deque()
        second_island_queue.append((start_row, start_col,0))
        grid[start_row][start_col] = 2
        
        while first_island_queue:
            curRow, curCol = first_island_queue.popleft()
            for dr, dc in directions:
                r = curRow + dr
                c = curCol + dc
                if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                    first_island_queue.append((r,c))
                    second_island_queue.append((r,c,0))
                    grid[r][c] = 2

        while second_island_queue:
            curRow, curCol, d= second_island_queue.popleft()

            for dr, dc in directions:
                r = curRow + dr
                c = curCol + dc

                if r in range(rows) and c in range(cols):
                    if grid[r][c] == 1:
                        return d
                    elif grid[r][c] == 0:
                        grid[r][c]= -1
                        second_island_queue.append((r,c,d+1))
        return 0