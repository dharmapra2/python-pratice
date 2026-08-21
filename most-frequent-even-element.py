from collections import Counter
from typing import List
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # seen = Counter(x for x in nums if x%2==0)
        # if not seen:
        #     return -1
        # return max(seen.keys(), key=lambda x: (seen[x], -x))
        freq = Counter(x for x in nums if x % 2 == 0)
        if not freq:
            return -1
        m = max(freq.values())
        res = min(x for x, v in freq.items() if v == m)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.mostFrequentEven([0, 1, 2, 2, 4, 4, 1]))  # Output: 2
    print(s.mostFrequentEven([4, 4, 4, 9, 2, 4]))     # Output: 4
    print(s.mostFrequentEven([29, 47, 21, 41, 13, 37])) # Output: -1