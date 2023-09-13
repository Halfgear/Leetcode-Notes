# [Problem Link](https://leetcode.com/problems/name-of-problem/description/)

# Intuition
Instead of focusing on moving zeros, I focused on placing the non-zero elements in their correct position. Once all the non-zero elements are in place, I can set remaining elements to zero.

# Approach
1. Maintain an index starting from 0. This will keep track of where I place the next non-zero element.

2. Iterate through the array using a loop.

3. For every non-zero element, place it at the position indicated by index and then increment index.

4. Fill the rest of the array after the index with zeros.

# Complexity
- Time complexity:
 O(n) where n is the number of elements in nums. We perform a single pass through the nums array.

- Space complexity:
 O(1). All operations are done in-place and we use a constant amount of space.

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
```