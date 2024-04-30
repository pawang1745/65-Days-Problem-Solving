class Solution:
    def isPerfectSquare(self, n):
        num = 1
        while n > 0:
            n -= num
            num += 2
        if n == 0:
            return 1
        else:
            return 0


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.isPerfectSquare(n))
