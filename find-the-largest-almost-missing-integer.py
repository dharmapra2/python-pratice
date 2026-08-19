# Problem: Find the Largest Almost Missing Integer (LC 3471)
#          Given nums and k, return the largest integer that appears in exactly one subarray of size k, or -1.
# Pattern: Sliding Window / Frequency Count
# Approach: Handle 3 cases:
#           1. k == n → every element is in exactly one subarray (the whole array), return max(nums)
#           2. k == 1 → every single element is its own subarray, return max of elements with count == 1
#           3. 1 < k < n → only nums[0] and nums[-1] can appear in exactly one subarray of size k;
#              check if their frequency is 1 and return the larger one
# Why this approach: For case 3, a subarray of size k slides from index 0 to n-k.
#                    nums[0] only appears in the first window, nums[-1] only in the last.
#                    All middle elements appear in at least 2 windows.
# Time: O(n)
# Space: O(n) for the Counter
# Mistake: Forgetting that middle elements always appear in multiple windows when 1 < k < n
# Key insight: Only boundary elements (first and last) can be "almost missing" when 1 < k < n

from typing import List
from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Case 1: k equals array length
        if k == n:
            return max(nums)
        
        counts = Counter(nums)
        
        # Case 2: k == 1
        if k == 1:
            uniques = [num for num, cnt in counts.items() if cnt == 1]
            return max(uniques) if uniques else -1
        
        # Case 3: 1 < k < n
        # Only boundary elements can appear in exactly one subarray of size k
        print(f"Counts: {counts}")
        ans = -1
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
        if counts[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    nums = [3,9,2,1,7]
    k= 3
    result = solution.largestInteger(nums,3)
    print(result)  # Output: 3
        