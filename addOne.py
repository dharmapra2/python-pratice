# Problem: Add One to a number represented as an array of digits.
#          Each element is a digit (0-9); return the array after incrementing by 1.
# Pattern: Array Traversal (Right to Left)
# Approach: Traverse from the last digit; if < 9 increment and return, else set to 0 and carry.
#           If all digits were 9, prepend 1.
# Why this approach: Simulates manual addition with carry in a single pass.
# Time: O(n)
# Space: O(1) — O(n) only in the all-9s edge case for the new array
# Mistake: Forgetting the all-9s edge case (e.g., [9,9,9] → [1,0,0,0])
# Key insight: Only digits equal to 9 propagate the carry; the first non-9 digit stops the loop.

class Solution:
    def addOne(self, arr):
        n = len(arr)
        
        # Traverse the array backwards (from right to left)
        for i in range(n - 1, -1, -1):
            # If the digit is less than 9, just increment it and we are done!
            if arr[i] < 9:
                arr[i] += 1
                return arr
            
            # If the digit is 9, it becomes 0 and the loop carries over to the left
            arr[i] = 0
            
        # If the loop finishes, it means all digits were 9 (e.g., [9, 9, 9] -> [0, 0, 0])
        # We need to insert a 1 at the very beginning
        return [1] + arr

sol = Solution()
arr = [5, 6, 7, 8]
print(sol.addOne(arr))
