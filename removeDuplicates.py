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
