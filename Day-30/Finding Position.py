class Solution:
    def nthPosition(self, n):
        position = 1
        while position * 2 <= n:
            position *= 2
        return position

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.nthPosition(n))
