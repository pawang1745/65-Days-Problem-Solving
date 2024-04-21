class Solution:
    def checkFibonacci(self, N):
        a, b = 0, 1
        while b <= N:
            if b == N:
                return "Yes"
            a, b = b, a + b
        return "No"

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())
    
        ob = Solution()
        print(ob.checkFibonacci(N))
