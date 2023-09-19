# [Problem Link](https://leetcode.com/problems/guess-number-higher-or-lower/dscription/)

# Intuition
The problem is a classic binary search scenario. By using the guess API, I could adjust my search boundaries.

# Approach
1. Initialize low at 1 and high at n.
2. Compute the mid of the range.
3. Apply the guess API on mid.
4. Depending on the API's response:
    - If 0, return mid.
    - If negative, adjust high to mid - 1.
    - If positive, adjust low to mid + 1

# Complexity
- Time complexity:
O(logn) due to binary search.

- Space complexity:
O(1), as no extra space is used.

# Code
```python
class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = int(low + (high-low)/2)
            res = guess(mid)

            if res == 0 : return mid
            elif res < 0 : high = mid - 1
            else: low = mid + 1
        
        return -1
```