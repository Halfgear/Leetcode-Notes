# [Problem Link](https://leetcode.com/problems/max-number-of-k-sum-pairs/description/)

# Intuition
The problem asks us to find the maximum number of pairs in an array nums that add up to a given integer k. Intuitively, I can approach this by sorting the array first and then using two pointers to find such pairs.

# Approach
1. First, I sort the array nums in ascending order.
2. I initialize two pointers left and right at the beginning and end of the array, respectively.
3. Then I iterate through the array:
    - If the sum of the numbers at the left and right pointers is less than k, I move the left pointer forward.
    - If the sum is greater than k, I move the right pointer backward.
    - If the sum is equal to k, it means I've found a pair. I increment the count of pairs and move both pointers inward.
# Complexity
- Time complexity:
O(n log n) for sorting the array, and O(n) for the two-pointer technique, making it overall O(n log n). This could be improved to be O(n) by using hashmap.

- Space complexity:
Space complexity: O(1) since we are using constant extra space. Using hashmap will increase the space complexity to O(n).

# Code
```python
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left=0
        right=len(nums)-1
        count = 0
        nums = sorted(nums)
        while left<right:
            if nums[left] + nums[right] < k:
                left+=1
            elif nums[left] + nums[right] > k:
                right-=1
            else:
                right-=1
                left+=1
                count+=1
        
        return count
```