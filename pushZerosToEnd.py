# Problem: Move all zeros to the end of an array while maintaining the relative order of non-zero elements.
# Pattern: Two Pointers (Read / Write)
# Approach: Use a write pointer that only advances on non-zero elements.
#           Swap arr[write] and arr[read] whenever a non-zero is found.
# Why this approach: In-place, single pass, preserves relative order of non-zero elements.
# Time: O(n)
# Space: O(1)
# Mistake: Overwriting instead of swapping — swap ensures zeros bubble to the back correctly.
# Key insight: The write pointer always points to the next slot for a non-zero element;
#              everything behind it is already clean.

class Solution:
    def pushZerosToEnd(self, arr):
        # 'write' tracks the position where the next non-zero element should go
        write = 0
        
        # 'read' iterates through the entire array
        for read in range(len(arr)):
            if arr[read] != 0:
                # Swap the non-zero element with the element at the write pointer
                arr[write], arr[read] = arr[read], arr[write]
                # Move the write pointer forward
                write += 1

        return arr

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    solution = Solution()
    solution.pushZerosToEnd(arr)

    print(arr)