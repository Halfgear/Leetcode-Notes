# [Problem Link](https://leetcode.com/problems/increasing-triplet-subsequence/description/)

# Intuition
My intuition relies on the fact that I can update the 'i' and 'j' if I found smaller value than previous ones. It will return True if it finds third value that are greater than i and j becuase that will be the third triplet.

# Complexity
- Time complexity:
It uses greedy approach which loops through the list only once, so the complexity is O(n)

- Space complexity:
Only saves constants without creating sepearte list, so it will be O(1)

# Code
```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # This float sets the value to infinity
        value1=float('inf')
        value2=float('inf')
        for n in nums:
            if n <= value1:
                value1 = n
            elif n <= value2:
                value2 = n
            else:
                return True
        return False
```