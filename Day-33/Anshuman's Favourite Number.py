class Solution:
    def isValid(self, N):
        # Check if the remainder of dividing N by 5 is either 0 or 5
        if N % 5 == 0 or N % 5 == 5:
            return "YES"
        else:
            return "NO"


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())
    

        ob = Solution()
        print(ob.isValid(N))
