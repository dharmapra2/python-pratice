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