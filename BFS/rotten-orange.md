# [Problem Link](https://leetcode.com/problems/name-of-problem/description/)

# Intuition

# Approach

# Complexity
- Time complexity:

- Space complexity:

# Code
```python
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        queue = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j,0))

        maxMin = 0
        while queue:
            curRow, curCol, curMin = queue.popleft()

            for dr, dc in directions:
                r = dr+curRow
                c = dc+curCol

                if r in range(row) and c in range(col) and grid[r][c] == 1:
                    queue.append((r,c, curMin+1))
                    grid[r][c] = 2
                if curMin > maxMin:
                    maxMin = curMin
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1

        return maxMin
```