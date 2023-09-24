# [Problem Link](https://leetcode.com/problems/min-cost-climbing-stairs/description/)

# Intuition
When I approached this problem, I wanted to calculate the minimum cost to reach each step, so I stored the cumulative minimum cost in a list called min_cost.

# Approach
1. I initialized an array min_cost of size (len(cost) + 1) to store the cumulative cost of reaching each step.
2. I started iterating from the third step (i = 2) since the first two steps would have a cost of 0.
3. For each step, I calculated the cost if I were to come from the previous step (one_step) and the cost if I were to come from the step before that (two_step).
4. I then chose the minimum of these two costs as the cost for the current step.
5. I stored this minimum cost in the min_cost array at the current index.
6. After iterating through all the steps, the last element of the min_cost array gives the minimum cost to reach the top.

# Complexity
- Time complexity: 
I iterated through the cost array once, so the time complexity is O(n), where n is the number of steps.

- Space complexity:
I used a single auxiliary list of size len(cost) + 1, so the space complexity is O(n), where n is the number of steps.

# Code
```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0] * (len(cost) + 1)
        
        for i in range(2, len(cost) + 1):
            one_step = min_cost[i - 1] + cost[i - 1]
            two_step = min_cost[i - 2] + cost[i - 2]
            min_cost[i] = min(one_step, two_step)

        return min_cost[-1]
```


