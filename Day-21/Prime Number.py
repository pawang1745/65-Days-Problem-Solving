import math

class Solution:
    # Function to check if a number is prime or not.
    def isPrime(self, N):
        if N <= 1:
            return 0  # N is not prime if it's less than or equal to 1

        # Iterate from 2 up to the square root of N
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                return 0  # N is not prime if it's divisible by any number other than 1 and itself

        return 1
            
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
