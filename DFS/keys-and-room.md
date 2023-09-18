# [Problem Link](https://leetcode.com/problems/keys-and-rooms/description/)

# Intuition
Upon examining this problem, I perceived the rooms and their keys as a representation of a graph, with rooms being nodes and keys serving as edges between nodes. I decided to start from the initial room (room 0), I could traverse to all other rooms by exploring the keys present in each room.

# Approach
My choice was to implement Depth-First Search (DFS) for this traversal, using a stack. I started with the first room (room 0) and marked it as visited. Every time I entered a room, I marked it as visited and added its keys to the stack. This process continued until the stack was empty. Upon completing the traversal, I loop visited List to check if all the rooms were marked as visited.

1. Initialize a stack and start with the first room (room 0).
2. For every room I enter, mark it as visited and add the unvisited rooms available through the keys to the stack.
3. Continue this DFS by popping and visiting rooms from the stack until it's emptied.
4. After the traversal, validate that all rooms were visited.

# Complexity
- Time complexity:
O(N + E) where N represents the number of rooms and E signifies the total number of keys. I ensured to process each room and each key just once.

- Space complexity:
O(N) which accounts for the visited list and the stack. In the most extensive scenario, all rooms could be on the stack simultaneously.

# Code
```python
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque()
        queue.append(0)
        n = len(rooms)
        visited = [-1] * (n)

        while queue:
            key = queue.pop()
            if visited[key] == -1:
                visited[key] = 1
                for value in rooms[key]:
                    queue.append(value)
                
        for visit in visited:
            if visit == -1:
                return False
        
        return True
```