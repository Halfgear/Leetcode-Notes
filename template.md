# [Problem Link](https://leetcode.com/problems/combination-sum-iii/description)

# Intuition
The problem asks for all possible combinations of k numbers that add up to a number n. The numbers should be from 1 to 9, and each number can be used only once. The approach taken here is backtracking, a well-known algorithmic technique for solving such combinatorial problems.

# Approach
1. An empty list results is defined to store the final combinations.
2. The function backtrack(remain, comb, next_start) is used to explore all combinations:
- remain is the remaining sum after considering elements in comb.
- comb is the current combination being considered.
- next_start is the next index to consider to avoid duplicates and reusing numbers.
3. Within backtrack, the base case checks if remain is zero and if comb has k elements. If both are true, a valid combination is found.
4. The function iterates through the possible numbers from next_start to 8 (since we are considering 1-based numbers, it effectively iterates through 1 to 9), updating comb and remain and recursing accordingly.

# Complexity
- Time complexity:
O(C(n,k)), where C(n,k) is the binomial coefficient. This is an upper bound because the algorithm explores all combinations of k numbers out of n (here (n=9).

- Space complexity:
O(k) to store the current combination. Also, recursion will take additional stack space, but that will also not exceed O(k)

# Code
```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                return

            for i in range(next_start, 9):
                comb.append(i+1)
                backtrack(remain-i-1, comb, i+1)
                comb.pop()

        backtrack(n, [], 0)

        return results
```