class Solution:
    def get_min_max(self, arr):
        if not arr: 
            return None
        arr.sort()
        return arr[0],arr[-1]
       