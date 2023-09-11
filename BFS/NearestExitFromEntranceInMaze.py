from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        rows = len(maze)
        cols = len(maze[0])

        queue = deque()
        for dr, dc in directions:
            r = entrance[0] + dr
            c = entrance[1] + dc
            if r in range(rows) and c in range(cols) and maze[r][c] == '.':
                maze[r][c] = '-'
                queue.append([r,c,1])

        maze[entrance[0]][entrance[1]] = '-'

        while queue:
            curRow, curCol, curCount = queue.popleft()

            for dr,dc in directions:
                r = curRow + dr
                c = curCol + dc
    
                if r in range(rows) and c in range(cols) and maze[r][c] == '.':
                    maze[r][c] = '-'
                    queue.append((r,c, curCount+1))

                if r not in range(rows) or c not in range(cols):
                    return curCount

        return -1
