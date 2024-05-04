import math

class Solution:
    def getHypotenuse(self, N):
        return math.floor(math.sqrt(4 * N))


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.getHypotenuse(N))
