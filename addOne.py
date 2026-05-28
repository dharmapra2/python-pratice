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
