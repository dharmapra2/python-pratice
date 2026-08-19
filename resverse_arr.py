# Problem: Reverse an array using multiple approaches.
# Pattern: Two Pointers / Recursion / Stack / Built-ins
# Approach: 6 methods shown —
#           1. Two pointers with temp variable (manual swap)
#           2. Slicing arr[::-1]
#           3. Built-in arr.reverse() (in-place)
#           4. Recursion: last element + reverse of rest
#           5. Stack: push all, pop all
#           6. Two pointers with tuple swap (Pythonic)
# Why this approach: Covers the full spectrum from O(1) space in-place to O(n) space methods.
# Time: O(n) for all approaches
# Space: O(1) for approaches 1, 3, 6 | O(n) for 2, 4, 5
# Mistake: In recursion (approach 4), forgetting the base case len <= 1 causes infinite recursion.
# Key insight: Two-pointer swap (approach 6) is the most Pythonic and optimal in-place solution.

class Solution:
    def reverseArray1(self, arr):
        """ using two pointer approach """
        # code here
        n = len(arr)
        for i in range(n // 2):
            temp = arr[i]
            arr[i] = arr[n - i - 1]
            arr[n - i - 1] = temp
        return arr

    def reverseArray2(self, arr):
        """ using slicing """
        # code here
        return arr[::-1]
    def reverseArray3(self, arr):
        """ using built-in reverse method """
        # code here
        arr.reverse()
        return arr
    def reverseArray4(self, arr):
        """ using recursion """
        # code here
        if len(arr) <= 1:
            return arr
        else:
            return [arr[-1]] + self.reverseArray4(arr[:-1])

    def reverseArray5(self, arr):
        """ using stack """
        # code here
        stack = []
        for item in arr:
            stack.append(item)
        reversed_arr = []
        while stack:
            reversed_arr.append(stack.pop())
        return reversed_arr

    def reverseArray6(self, arr):
        """ using two pointers """
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

if __name__ == "__main__":
    sol= Solution()
    arr = [1, 2, 2, 3, 4, 4, 4, 5]
    print(sol.reverseArray6(arr))