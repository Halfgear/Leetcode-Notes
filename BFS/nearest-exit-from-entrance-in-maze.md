# [Problem Link](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/)

# Intuition
To find the nearest exit in a maze, I use Breadth First Search (BFS) because BFS explores the neighboring cells at the current level before moving on to cells that are two steps away. This ensures that as soon as we encounter outside of border, it's the closest one.

# Approach
1. Define bfs movement directions (up, down, left, right).
2. Initialize a queue with the entrance as the starting point and a counter set to 1. The starting point added neighbors only if they are valid empty block. No border and wall.
3. While the queue is not empty, for each point:

    - Dequeue the point.

    - Check all 4 neighboring points using directions.

    - If a neighboring point is within the bounds of the maze and is a '.', mark it as visited (set to '-') and enqueue it with a counter incremented by 1.

    - If the point is on the boundary of the maze, return the counter as that would be the shortest path to exit.

4. If the queue gets exhausted without finding an exit, return -1 to indicate no path exists.


# Complexity
- Time complexity:
The worst-case time complexity is O(n×m), where n is the number of rows and m is the number of columns. This is simply because, I may need to visit all the cells of the maze.

- Space complexity:
The worst-case space complexity is also O(n×m) because in a scenario where every cell is accessible, we might have to store all of them in the queue.

# Code
```python
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
```