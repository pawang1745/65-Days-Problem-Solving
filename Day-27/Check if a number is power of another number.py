import math
class Solution:
    def isPowerOfAnother(self, X: int, Y: int) -> bool:
        if Y <= 0 or X <= 1:  
            return 0
        max_power = int(math.log(Y, X))  

        while X ** max_power > Y:  
            max_power -= 1

        if X ** max_power == Y:
            return 1
        else:
            return 0
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        X,Y=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.isPowerOfAnother(X,Y))
