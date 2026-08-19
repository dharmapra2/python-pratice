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