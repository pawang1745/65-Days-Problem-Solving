class Solution:
    def countSquares(self, N):
        sqrt_N = int(math.sqrt(N))
        return sqrt_N - 1 if sqrt_N * sqrt_N == N else sqrt_N

import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countSquares(N))
