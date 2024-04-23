class Solution:
    def differenceSeries(self, N):
        if N <= 0:
            raise ValueError("N must be a positive integer")

        # Formula for the Nth term: N * (2 * N + 1)
        return N * (2 * N + 1)            


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.differenceSeries(N)
        print(ans)
