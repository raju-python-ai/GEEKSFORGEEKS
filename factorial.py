# Input: n = 5
# Output: 120
# Explanation: 1 x 2 x 3 x 4 x 5 = 120
class Solution:
    def factorial (self, n):
        val=1
        for i in range(1,n+1):
            val*=i
        return val
