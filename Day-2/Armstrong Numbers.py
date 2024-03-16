class Solution:
    def armstrongNumber (self, n):
        # code here 
        d1=n//100
        d2=(n//10)%10
        d3=n%10
        
        if n==(d1**3+d2**3+d3**3):
            return "Yes"
        else:
            return "No"
        

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
