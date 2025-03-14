#User function Template for python3
class Solution:
    def rotate(self, arr):
        if not arr:  
            return
        
        last_element = arr.pop()  
        arr.insert(0, last_element) 