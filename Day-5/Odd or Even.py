
class Solution:
    def oddEven (ob,N):
        # code here 
        if N%2==0:
            return "even"
        else:
            return "odd"

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())

        ob = Solution()
        print(ob.oddEven(N))
