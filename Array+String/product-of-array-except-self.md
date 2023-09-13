# [Problem Link](https://leetcode.com/problems/product-of-array-except-self/description/)

# Intuition
To calculate the product of the array except for the current element, I can think of this product as the product of all numbers to the left of the current element multiplied by all numbers to the right of the current element.

# Approach
1. Create two lists left_list and right_list.
2. Populate both list such that every element at i is the product of all numbers to the left and right of i in nums.
3. For every index i in nums, the product of left_list[i] and right_list[i] will give the result for that index.

# Memory Optimized Approach
1. Initialize the output array with a single 1 because there is no number to the left of the first element.
2. For each number in nums from the second number onward, calculate the product of all numbers to its left and append it to the output.
3. Then, iterate over nums backward, multiplying each output value by the product of all numbers to the right of the corresponding nums value.

# Complexity
- Time complexity:
O(n) as we make two or three separate passes over the nums array.

- Space complexity:
O(n) for the space required by the left_list, right_list, and output.

- Memory Optimized Space complexity
O(1) ignoring the space needed for the output array since I did not use any additional data structures.

# Code
```python
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        n = len(nums)
        if not nums:
            return []

        left_list = [1]
        right_list = [1]

        left = 1
        right = 1
        
        for i in range(1,n):
            left *= nums[i-1]
            left_list.append(left)

        for j in range(n-1, 0, -1):
            right *= nums[j]
            right_list.append(right)
        
        right_list = list(reversed(right_list))
    
        for i in range(n):
            output.append(left_list[i]*right_list[i])

        return output
```

# Memory Optimized Code
```python
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        if not nums:
            return []

        left = 1
        right = 1
        for i in range(1,len(nums)):
            left *= nums[i-1]
            output.append(left)

        for j in range(len(nums)-1, 0, -1):
            right *= nums[j]
            output[j-1] = output[j-1]*right
        
        return output
```