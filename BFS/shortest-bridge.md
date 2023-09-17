# [Problem Link](https://leetcode.com/problems/shortest-bridge/)

# Intuition
To find the shortest bridge, I first needed to identify one island and then try to expand from this island to reach the other island in shortest path. Each level of expansion is a BFS (Breadth-First Search) layer until I hit the second island.

# Approach
1. loop through the matrix to find the first cell that belongs to one of the islands (represented by value 1). Start a BFS to label this entire island to another distinct number (say 2).

2. After the first island is labeled, start another BFS from all the 2 labeled cells. The BFS will go layer by layer. If it hits the original value 1, it means I've reached the second island, and the number of layers you've traversed will be the shortest bridge.

    - This could be more optimized by starting only at the border of 2 labeled cells.

3. If during the BFS, If reached a cell with value 0 (water), I marked it -1 and continue the BFS in subsequent layers.

# Complexity
- Time complexity:
The worst-case time complexity is O(n^2), where n is the number of rows and columns. This is simply because, I may need to visit all the cells of the island and water.

- Space complexity:
The worst-case space complexity is also O(n^2) because in a scenario where every cell is island, I might have to store all of them in the fisrt queue.


```python
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
```