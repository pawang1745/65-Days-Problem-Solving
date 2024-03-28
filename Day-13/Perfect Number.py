class Solution:
    def isPerfect(self, N):
        num_str = str(N)
        def factorial(n):
            if n == 0:
                return 1
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            return fact
        sum_of_factorial = sum(factorial(int(digit)) for digit in num_str)
        if sum_of_factorial == N:
            return 1
        else:
            return 0


if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isPerfect(N))   
