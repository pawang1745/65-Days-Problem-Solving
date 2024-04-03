class Solution:
    def clockSum(self, num1, num2):
        # code here
        sum=num1+num2
        return sum % 12 if sum > 0 else sum + 12


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        num1, num2 = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.clockSum(num1, num2))
