
class Solution:
    def mean(self, N , A):
        # code here
        sum=0
        for i in range(N):
            sum+=A[i]
            
        return sum//N
            

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A = list(map(int,input().split()))
        
        ob = Solution()
        print(ob.mean(N,A))
