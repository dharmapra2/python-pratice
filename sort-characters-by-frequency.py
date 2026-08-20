from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        out = ""
        word = Counter(s)
        word = sorted(word.items(), key=lambda pair: -pair[1])
        l = dict(word)

        for key, value in l.items():
            s = key * value
            out += s

        return out


if __name__ == "__main__":
    s = "tree"
    solution = Solution()
    print(solution.frequencySort(s))  # Output: "eert" or "eetr"   