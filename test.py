# ─────────────────────────────────────────────────────────────
# Problem: Concatenation of Array (LC 1929)
#          Given nums of length n, return ans of length 2n where ans = nums + nums.
# Pattern: Array Index Mapping
# Approach: Create ans of size 2n, then for each index i set ans[i] = ans[i+n] = nums[i].
# Why this approach: Single pass, no extra library, directly maps both halves simultaneously.
# Time: O(n)
# Space: O(n)
# Mistake: Using ans = nums + nums (works but less instructive for index practice).
# Key insight: ans[i] and ans[i+n] are always the same value — assign both in one step.
# ─────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────
# Problem: Valid Anagram (LC 242)
#          Given two strings s and t, return True if t is an anagram of s.
# Pattern: Hash Map / Frequency Count
# Approach: Count character frequencies in s, then decrement for each char in t.
#           Return False if a char is missing or count hits 0 prematurely.
# Why this approach: O(n) single-pass counting without sorting.
# Time: O(n)
# Space: O(1) — at most 26 keys for lowercase letters
# Mistake: Not checking length equality upfront — saves time on obvious mismatches.
# Key insight: Two strings are anagrams iff their character frequency maps are identical.
# ─────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────
# Problem: Valid Palindrome (LC 125)
#          A phrase is a palindrome if, after lowercasing and keeping only alphanumerics,
#          it reads the same forwards and backwards.
# Pattern: Two Pointers
# Approach: Filter to alphanumeric lowercase chars, then use left/right pointers moving inward.
# Why this approach: Clean separation of filtering and checking; O(n) time and space.
# Time: O(n)
# Space: O(n) for the filtered list
# Mistake: Not stripping non-alphanumeric chars before comparing — spaces/punctuation break it.
# Key insight: isalnum() + lower() handles all edge cases cleanly before the two-pointer check.
# ─────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────
# Problem: Palindrome Partitioning (LC 131)
#          Given string s, return all possible partitions where every substring is a palindrome.
# Pattern: Backtracking
# Approach: At each index, try every substring starting there; if it's a palindrome, add it
#           to current partition and recurse. Backtrack by popping after recursion.
# Why this approach: Explores all valid partitions without generating invalid ones.
# Time: O(n * 2^n) — 2^n subsets, O(n) palindrome check each
# Space: O(n) recursion depth
# Mistake: Not backtracking (popping curr) after recursion — causes stale state in curr.
# Key insight: Build the substring incrementally (temp += s[i]) to avoid repeated slicing.
# ─────────────────────────────────────────────────────────────

def outer_func():
    msg = 'Hello there!'
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        global res  # Allow modification of an enclosing variable
        res = 'How are you?'
        print(msg)  # Accessing msg from outer_func()

    inner_func()
    print(f"res: {res}")  # Now res is accessible and modified

# outer_func()
# print(res)  # Now res is accessible and modified




numbers = [1, 2, 3, 4, 5]
name, age, *job = (numbers)
# numbers[7]
# print(list(numbers))
# if 3 in numbers:
#     print("3 is in the numbers list.")
# print(tuple(numbers))
# print(set(numbers))

# print(numbers[0:3])  # Slicing the list to get the first three elements
# print(numbers[-2:])  # Slicing the list to get the last two elements


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[0]*(2* n)
        print(ans)
        for i,num in enumerate(nums):
            ans[i] = ans[i+n] = num
        return ans
    
# solution = Solution()
# print(solution.getConcatenation([1, 2, 3]))


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True
    

class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = [e.lower() for e in s if e.isalnum()]
        verif = True
        left, right = 0, len(letters) - 1
        print(f"letters: {letters}, left: {left}, right: {right}")
        while verif and left < right:
            if letters[left] != letters[right]:
                verif = False
            left += 1
            right -= 1
        return verif

solution = Solution()
# print(solution.isPalindrome("A man a plan a canal Panama"))


# Check if the string is a palindrome
def isPalindrome(s):
    return s == s[::-1]

# Backtracking function to generate all palindromic partitions
def backtrack(idx, s, curr, res):
    print(f"idx: {idx}, s: {s}, curr: {curr}, res: {res}")
    if idx == len(s):
        # Save the current valid partition
        res.append(curr[:])  
        return

    temp = ""
    for i in range(idx, len(s)):
        temp += s[i]
        print(f"item : {temp}")
        if isPalindrome(temp):
            # Choose substring
            curr.append(temp)              
            # Explore further
            backtrack(i + 1, s, curr, res) 
            # Backtrack
            curr.pop()  
        print(f"curr : {curr}, res : {res}")                   

# Generate all palindromic partitions and sort them
def palinParts(s):
    res = []
    backtrack(0, s, [], res)
    return res

if __name__ == "__main__":
    s = "geeks"
    res = palinParts(s)
    for part in res:
        print(" ".join(part))