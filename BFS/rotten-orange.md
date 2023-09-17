# [Problem Link](https://leetcode.com/problems/rotting-oranges/description/)

# Intuition
This question is basic BFS search question. I need to find all rotten orange first, start BFS on every orange, track the time, and check if it had any fresh orange left.

# Approach
1. Find all rotten Oranges to start spreading and add them to queue.
2. Spread the rottening to four directions. If if found an new fresh orange, make it rotten and add it to the queue.
3. Loop until there is no more orange to spread.
4. Check if there is any fresh orange left. If there is, return -1.
5. If there is no fresh orange, return the tracked mins to finish looping.

# Complexity
- Time complexity:
The worst-case time complexity is O(n×m), where n is the number of rows and m is the number of columns. This is simply because, I may need to visit all cells in the grid.

- Space complexity:
The worst-case space complexity is also O(n×m) because in a scenario where every orange is rotten, I might have to append all of them in the queue.

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