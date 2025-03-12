#User function Template for python3

class Solution:
    def armstrongNumber (self, n):

        return n == sum(int(digit) ** 3 for digit in str(n))
