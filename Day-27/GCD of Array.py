import math

class Solution:
    def gcd(self, n, arr):
        if n == 0:
            return None
        result = arr[0]
        for i in range(1, n):
            result = math.gcd(result, arr[i])
        return result

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.gcd(n,arr))
