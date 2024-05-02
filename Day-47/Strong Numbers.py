class Solution:
    def isStrong(self, N):
        original_number = N
        digit_factorial_sum = 0
        
        # Function to calculate the factorial of a number
        def factorial(num):
            if num == 0 or num == 1:
                return 1
            return num * factorial(num - 1)
        
        # Calculate the sum of factorials of digits
        while N > 0:
            digit = N % 10
            digit_factorial_sum += factorial(digit)
            N //= 10
        
        # Check if the sum of factorials is equal to the original number
        if digit_factorial_sum == original_number:
            return 1
        else:
            return 0



import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isStrong(N))
