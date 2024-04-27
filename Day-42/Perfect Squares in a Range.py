class Solution:
    def numOfPerfectSquares(self, a, b):
        # Calculate the square root of a and b
        sqrt_a = int(a ** 0.5)
        sqrt_b = int(b ** 0.5)
        
        # Initialize the count of perfect squares
        count = 0
        
        # Iterate from sqrt_a to sqrt_b (inclusive)
        for i in range(sqrt_a, sqrt_b + 1):
            square = i * i
            if a <= square <= b:
                count += 1
        
        return count

import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b=map(int,input().split())
        
        ob = Solution()
        print(ob.numOfPerfectSquares(a,b))
