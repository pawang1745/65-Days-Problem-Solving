import math
class Solution:
    def cubeRoot(self, N):
        # code here
        if N < 0:
            return -math.pow(-N, 1/3)  # Handle negative numbers
        else:
            return int(math.pow(N, 1/3))


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.cubeRoot(N))
