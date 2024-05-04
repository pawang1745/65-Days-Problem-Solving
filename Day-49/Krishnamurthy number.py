class Solution:
    def isKrishnamurthy(self, N):
        # Function to calculate the factorial of a number
        def factorial(num):
            if num == 0 or num == 1:
                return 1
            else:
                return num * factorial(num - 1)

        # Calculate the sum of factorials of digits
        digit_sum = sum(factorial(int(digit)) for digit in str(N))

        # Check if the sum equals the number
        if digit_sum == N:
            return "YES"
        else:
            return "NO"



import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isKrishnamurthy(N))
