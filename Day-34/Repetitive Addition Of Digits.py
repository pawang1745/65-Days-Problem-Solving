class Solution:
    def singleDigit(self, N):
    	#code here 
    	while N >= 10:
            N = sum(int(digit) for digit in str(N))
        return N
    	    


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.singleDigit(N)
        print(ans)
