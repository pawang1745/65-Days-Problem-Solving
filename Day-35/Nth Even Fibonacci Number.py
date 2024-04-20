class Solution:
    def nthEvenFibonacci(self, n):
        # Initialize the first two Fibonacci numbers
        a, b = 0, 1
        
        # Initialize variables to keep track of the current Fibonacci number and its index
        current_index = 0
        current_fibonacci = 0
        
        # Iterate until we find the nth even Fibonacci number
        while current_index < n:
            # Calculate the next Fibonacci number
            a, b = b, a + b
            
            # If the Fibonacci number is even, increment the index and update the current even Fibonacci number
            if b % 2 == 0:
                current_index += 1
                current_fibonacci = b
        
        # Return the nth even Fibonacci number modulo 10^9 + 7
        return current_fibonacci % 1000000007

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.nthEvenFibonacci(n))
