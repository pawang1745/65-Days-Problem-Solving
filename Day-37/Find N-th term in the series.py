
class Solution:
    def nthOfSeries (self, n):
        # code here 
        return 8 * n**2 + 1
        

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.nthOfSeries(n))
