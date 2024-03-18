
class Solution:
    def addition (ob,A,B):
        # code here
        ob=A+B
        return ob

if __name__ == '__main__': 
    t = int (input())
    for _ in range (t):
        
        A,B=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.addition(A,B))
