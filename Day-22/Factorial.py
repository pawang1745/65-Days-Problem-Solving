class Solution:
    def factorial(self, N):
        if N == 0 or N == 1:
            return 1
        factorial_value = 1
        for i in range(2, N + 1):
            factorial_value *= i
        return factorial_value


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.factorial(N))
