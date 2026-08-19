# Problem:
# Pattern:
# Approach:
# Why this approach:
# Time:
# Space:
# Mistake:
# Key insight:
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
        