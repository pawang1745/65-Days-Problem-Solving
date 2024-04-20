import math

class Solution:
    def isPowerofFour(self, n):
        # Check if n is positive and if log base 4 of n is an integer
        return n > 0 and math.log(n, 4).is_integer()


if __name__=='__main__':
    test = int(input())
    for i in range(test):
        num = int(input())
        if(Solution().isPowerofFour(num)):
            print (1)
        else:
            print (0)
