# Input: n = 7
# Output: true
# Explanation: 7 has exactly two divisors: 1 and 7, making it a prime number.
class Solution:
    def isPrime(self, n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
