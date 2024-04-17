class Solution:
    def mthHalf(self, N, M):
        # Start halving N M-1 times
        for _ in range(M - 1):
            N //= 2
        return N

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.mthHalf(N, M))
