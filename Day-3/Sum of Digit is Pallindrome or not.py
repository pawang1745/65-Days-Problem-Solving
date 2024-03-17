class Solution:
    def isDigitSumPalindrome(self, n):
        #code here
        # Function to calculate the sum of digits
        def digit_sum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total
        
        # Function to check if a number is palindrome
        def is_palindrome(num):
            return str(num) == str(num)[::-1]
        
        # Calculate the sum of digits
        sum_of_digits = digit_sum(n)
        
        # Check if the sum of digits is a palindrome
        if is_palindrome(sum_of_digits):
            return 1
        else:
            return 0


if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
