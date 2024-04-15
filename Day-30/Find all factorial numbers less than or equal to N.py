class Solution:
    def factorialNumbers(self, N):
        result = []
        factorial = 1
        i = 1
        while factorial <= N:
            result.append(factorial)
            i += 1
            factorial *= i
        return result
    	


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()
        
