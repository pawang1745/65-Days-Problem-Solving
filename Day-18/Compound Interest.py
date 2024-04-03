class Solution:
    def getCompundInterest(self, P ,T , N , R):
        # code here
        R_decimal = R / 100
        A = P * math.pow(1 + R_decimal / N, N * T)
        return math.floor(A)

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        P,T,N,R = map(int,input().split())
        
        ob = Solution()
        print(ob.getCompundInterest(P,T,N,R))
