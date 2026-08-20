from collections import Counter
import heapq
from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        seen = Counter(words)
        return heapq.nsmallest(k, seen.keys(), key=lambda word: (-seen[word], word))
        # frequentWords = sorted(seen.items(), key=lambda pair: (-pair[1], pair[0]))
        # return [wor÷ for word, count in frequentWords[:k]]
    
    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        s = list(set(words))
        s.sort(key = lambda x: (-c[x], x))
        return s[:k]


if __name__ == "__main__":
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    solution = Solution()
    print(solution.topKFrequent(words, k))  # Output: ["i", "love"]
    print(solution.topKFrequent2(words, k))  # Output: ["i", "love"]