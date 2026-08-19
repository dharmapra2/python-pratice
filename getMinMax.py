# Problem: Find the minimum and maximum element in an array.
# Pattern: Pair Comparison / Tournament Method
# Approach: Initialize min/max from the first pair, then process remaining elements in pairs.
#           Compare the two elements of each pair against each other first, then update min/max.
# Why this approach: Processing in pairs reduces comparisons from 2*(n-1) to ~1.5*n,
#                    which is the optimal comparison count.
# Time: O(n)
# Space: O(1)
# Mistake: Not handling the odd-length array edge case (single leftover element at the end).
# Key insight: Comparing pairs internally before comparing with global min/max saves one comparison per pair.

class Solution:
    def getMinMax(self, arr):
        n = len(arr)
        if n == 1:
            return [arr[0], arr[0]]
            
        # Initialize min and max
        if arr[0] > arr[1]:
            curr_max, curr_min = arr[0], arr[1]
        else:
            curr_max, curr_min = arr[1], arr[0]
            
        # Process remaining elements in pairs
        for i in range(2, n, 2):
            if i == n - 1:  # Single remaining element if odd length
                curr_min = min(curr_min, arr[i])
                curr_max = max(curr_max, arr[i])
            else:
                if arr[i] > arr[i + 1]:
                    curr_max = max(curr_max, arr[i])
                    curr_min = min(curr_min, arr[i + 1])
                else:
                    curr_max = max(curr_max, arr[i + 1])
                    curr_min = min(curr_min, arr[i])
                    
        return [curr_min, curr_max]

if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 2, 3, 4, 4, 4, 5]
    print(sol.getMinMax(arr))