class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)
    
    def getSmallestDivNum(self, n): 
        if n == 1:
            return 1
        
        lcm_val = 1
        for i in range(2, n + 1):
            lcm_val = self.lcm(lcm_val, i)
        
        return lcm_val
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        ob = Solution()
        print(ob.getSmallestDivNum(n))
