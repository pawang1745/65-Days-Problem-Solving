class Solution:
    def find (self, N):
        # code here
        return N+1



if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.find(N))
