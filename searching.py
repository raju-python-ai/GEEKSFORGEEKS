
# Input: k = 16 , arr = [9, 7, 16, 16, 4]
# Output: 3
# Explanation: The value 16 is found in the given array at positions 3 and 4, with position 3 being the first occurrence.from typing import List

class Solution:
    def search(self, k: int, arr: List[int]) -> int:
        # code here
        for i in range(len(arr)):
            if  k==arr[i]:
                return i+1
        return -1