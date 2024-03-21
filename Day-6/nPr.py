
import math
class Solution:
    def nPr(self, n, r):
        # code here
        
        return math.factorial(n)//math.factorial(n-r)



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nPr(n, r))
