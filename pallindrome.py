# Input: arr[] = [111, 222, 333, 444, 555]
# Output: true
# Explanation:
# arr[0] = 111, which is a palindrome number.
# arr[1] = 222, which is a palindrome number.
# arr[2] = 333, which is a palindrome number.
# arr[3] = 444, which is a palindrome number.
# arr[4] = 555, which is a palindrome number.
# As all numbers are palindrome so This will return true.
def isPalinArray(arr):
    val=0
    for i in range (len(arr)):
        string=str(arr[i])
        if string==string[::-1]:
            val=1
        else:
            return 0
    return val
