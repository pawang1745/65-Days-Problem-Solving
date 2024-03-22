class Solution:
    def oppositeFaceOfDice(self, N):
    	#code here 
    	opp_face=7-N
    	return opp_face


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.oppositeFaceOfDice(N)
        print(ans)
