from collections import Counter
from typing import List

class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in Counter(nums).most_common(k)]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # buckets[i] will store all numbers that appear exactly i times
        buckets = [[] for _ in range(len(nums) + 1)]
        print(buckets)
        for num, freq in count.items():
            print(f"num: {num}, freq: {freq}")
            buckets[freq].append(num)

        print(buckets)

            
        res = []
        # Traverse from highest possible frequency down to 1
        for freq in range(len(buckets) - 1, 0, -1):
            print(f"freq: {freq}, buckets[freq]: {buckets[freq]}")
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    solution = Solution()
    print(solution.topKFrequent(nums, k))  # Output: [1, 2]