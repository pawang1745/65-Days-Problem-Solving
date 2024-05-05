class Solution:
    def findArea(self, A, B, C):
        s = (A + B + C) / 2
        if s * (s - A) * (s - B) * (s - C) <= 0:
            return 0.000
        area = (s * (s - A) * (s - B) * (s - C)) ** 0.5
        return round(area, 3)



import math
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split(' '))
        ob=Solution()
        print("%.3f"%ob.findArea(A,B,C))
