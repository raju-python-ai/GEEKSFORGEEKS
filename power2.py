class Solution:
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self, n):
        # code here
    #   if n <= 0:
    #     return False
      return (n & (n - 1)) == 0
