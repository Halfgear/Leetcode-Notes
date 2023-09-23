# [Problem Link](https://leetcode.com/problems/n-th-tribonacci-number/)

# Intuition
To solve this problem, one can think of it as an extension of the Fibonacci sequence, but instead of two preceding numbers, I had to consider three. Therefore, a Dynamic Programming (DP) approach seems suitable.
# Approach
- Base Case: The solution checks if n is less than 3, and if so, directly returns the base case.

- Initialization: The code then initializes an array dp of size n + 1 with all values as 0. The values dp(1) and dp(2) are both set to 1.

- DP Calculation: From index 3 to n, the solution calculates the Tribonacci number using the relation: T(i) = T(i-1) + T(i-2) + T(i-3).

- Return: the nth Tribonacci number is the value at index n in the dp array.

# Complexity
- Time complexity:
The code iterates through the numbers 3 to n once to populate the DP table. Thus, it is O(n).

- Space complexity:
The space used is for the DP table of size n + 1, so it's O(n).

# Code
```python
class Solution:
    def tribonacci(self, n: int) -> int:
        if n<3:
            return 1 if n else 0
        dp = [0] * (n + 1)
        dp[1] = dp[2] = 1

        for i in range(3, n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        
        return dp[n]
```