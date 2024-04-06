class Solution:
    # Function to return a list containing the first n Fibonacci numbers.
    def printFibb(self, n):
        fib_list = []  # Initialize an empty list to store Fibonacci numbers

        # Base case: the first two Fibonacci numbers are always 1
        if n >= 1:
            fib_list.append(1)
        if n >= 2:
            fib_list.append(1)

        # Generating Fibonacci numbers starting from the 3rd index
        for i in range(2, n):
            fib_list.append(fib_list[-1] + fib_list[-2])

        return fib_list


if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
