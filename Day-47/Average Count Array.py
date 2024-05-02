class Solution:
    def countArray(self, arr, n, x):
        result = [0] * n  # Initialize the resultant array with zeros
        for i in range(n):
            avg = (arr[i] + x) // 2  # Calculate the floor value of the average
            count = 0
            for j in range(n):
                if (arr[j] == avg):
                    count += 1
            result[i] = count
        return result




for _ in range(0,int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    ans = Solution().countArray(arr, n, x)
    print(*ans)
