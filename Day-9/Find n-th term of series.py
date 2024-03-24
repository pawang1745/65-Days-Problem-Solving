class Solution:
    def findNthTerm(self, N):
        # code here 
        a=N*(N+1)//2
        return a


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.findNthTerm(N))
