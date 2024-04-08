class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return abs(a * b) // self.gcd(a, b)

    def lcmAndGcd(self, A, B):
        gcd_val = self.gcd(A, B)
        lcm_val = self.lcm(A, B)
        return lcm_val, gcd_val

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
