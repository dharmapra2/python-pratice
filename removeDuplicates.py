# Problem: Remove duplicates from a sorted array in-place and return the unique portion.
# Pattern: Two Pointers (Read / Write) on sorted array
# Approach: write pointer tracks the last unique element's index.
#           read pointer scans forward; when arr[read] != arr[write], advance write and copy.
#           Return arr[:write+1].
# Why this approach: Sorted array guarantees duplicates are adjacent, so a single pass suffices.
# Time: O(n)
# Space: O(1) — modifies in place (slice at return is O(k) where k = unique count)
# Mistake: Starting read from 0 instead of 1 — comparing element with itself causes off-by-one.
# Key insight: write pointer always points to the boundary of the "clean" unique prefix.

class Solution:
    def removeDuplicates(self, arr):
        # return list(dict.fromkeys(arr))
        if not arr:
            return []
        
        # 'write' pointer tracks the index of the last unique element
        write = 0
        
        for read in range(1, len(arr)):
            print(read, write, arr)
            if arr[read] != arr[write]:
                write += 1
                arr[write] = arr[read]
        
        # Slice the array from the beginning up to the 'write' pointer (+1 to include it)
        # This returns the modified unique portion of the list
        print(arr)
        return arr[:write + 1]

if __name__ == "__main__":
    sol= Solution()
    arr = [1, 2, 2, 3, 4, 4, 4, 5]
    print(sol.removeDuplicates(arr))
