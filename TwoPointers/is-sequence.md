# [Problem Link](https://leetcode.com/problems/is-sequence/description/)

# Intuition and Approach
The intuition behind this problem is that I can traverse both strings using two pointers. If the character at the current position of string s matches the character at the current position of string t, I move the pointer of string s forward. The goal is to move through all of string s while still having characters left in t.

# Complexity
- Time complexity:
O(n), where n is the length of string t. In the worst case, I will traverse the entire length of t.

- Space complexity:
O(1), as I used only two pointers and a few other constant space variables.I did not use any additional data structures that grow with the size of the used space.

# Code
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0

        if len(s) == 0: return True

        while t_pointer < len(t) and s_pointer < len(s):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            if s_pointer == len(s):
                return True
            t_pointer += 1

        return False
```