# Input: n = 4
# Output: true
# Explanation: 4 is not divisible by 100 and is divisible by 4 so its a leap year
class Solution:
    def checkYear(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False