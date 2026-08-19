# Problem: Find the missing number in an array containing n distinct numbers from range [0, n].
# Pattern: Math (Gauss Sum)
# Approach: Compute expected sum of 0..n using n*(n+1)//2, subtract actual sum of array.
#           The difference is the missing number.
# Why this approach: Single pass, no extra space, no sorting needed.
# Time: O(n)
# Space: O(1)
# Mistake: Using range [1, n] instead of [0, n] — the range includes 0.
# Key insight: Expected sum minus actual sum isolates exactly the one missing value.

# missingNumber is a function that takes a list of numbers and returns the missing number in the sequence. The function assumes that the input list contains n distinct numbers taken from the range 0 to n, with one number missing.Here is a possible implementation of the `missingNumber` function in Python:

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 2, 3, 5]
    print(sol.missingNumber(nums))  # Output: 4