# Input: a = 13, b = 9
# Output: 9 13
# Explanation: After swapping it becomes 9 and 13.
class Solution:
    def get(self, a, b):
        temp = a
        a = b
        b = temp

        return a, b  
