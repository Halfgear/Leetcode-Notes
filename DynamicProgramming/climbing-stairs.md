# [Problem Link](https://leetcode.com/problems/climbing-stairs/description/)

# Intuition
The problem asks for the number of distinct ways to climb a staircase. Each step I can either take 1 step or 2 steps. Given that, the number of distinct ways to climb n stairs is the sum of the number of distinct ways to climb n-1 stairs and n-2 stairs. This is because I can reach the nth stair either by taking a 1-step from the n-1th stair or a 2-step from the n-2th stair.

# Approach
I used dynamic programming to solve this problem. I created an array dp where dp[i] will store the number of distinct ways to climb i stairs.

- For n = 1, there is only 1 way to climb, so dp[1] = 1.
- For n = 2, there are 2 ways to climb, either two 1-steps or one 2-step, so dp[2] = 2.
After initializing the base cases, I loop through 3 to n to populate the dp array based on the formula: dp[i] = dp[i-1] + dp[i-2].

# Complexity
- Time complexity: O(n), as I iterate through the array once.
- Space complexity: O(n) for storing the dp array.
# Code
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n] 
```
        