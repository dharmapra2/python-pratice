# Problem: Find the Kth smallest element in an unsorted array.
# Pattern: Heap (Max-Heap of size k)
# Approach: Maintain a max-heap of size k. For each element, if it's smaller than the heap's
#           root (largest in heap), replace the root. The root at the end is the kth smallest.
# Why this approach: Avoids full sort; only tracks the k smallest elements seen so far.
# Time: O(n log k)
# Space: O(k)
# Mistake: Using a min-heap directly gives the smallest, not the kth smallest without extra work.
#          Negating values simulates a max-heap using Python's min-heap (heapq).
# Key insight: A max-heap of size k always holds the k smallest elements;
#              its root is the largest among them — i.e., the kth smallest.

import heapq

class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        max_heap = []

        for num in arr:
            if len(max_heap) < k:
                heapq.heappush(max_heap, -num)
                print(f"Heap after pushing {-num}: {[-x for x in max_heap]}")
            elif -num > max_heap[0]:
                # If current number is smaller than the largest in the heap
                heapq.heapreplace(max_heap, -num)

        # The root contains the negative of the kth smallest element
        return -max_heap[0]

if __name__ == "__main__":
    sol = Solution()
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    print(sol.kthSmallest(arr, k))