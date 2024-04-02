class Solution:
    def getAreas(self, L , W , B , H , R):
        # code here
        rectangle_area = L * W
        triangle_area = int(0.5 * B * H)
        circle_area = int(3.14 * (R**2))
        return rectangle_area, triangle_area, circle_area

 import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        L,W,B,H,R=map(int,input().split())
        
        ob = Solution()
        ptr = ob.getAreas(L,W,B,H,R)
        
        print(ptr[0],ptr[1],ptr[2])
