class Solution:
    def pushZerosToEnd(self, arr):
        # 'write' tracks the position where the next non-zero element should go
        write = 0
        
        # 'read' iterates through the entire array
        for read in range(len(arr)):
            if arr[read] != 0:
                # Swap the non-zero element with the element at the write pointer
                arr[write], arr[read] = arr[read], arr[write]
                # Move the write pointer forward
                write += 1

        return arr

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    solution = Solution()
    solution.pushZerosToEnd(arr)

    print(arr)