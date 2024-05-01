class Solution:
    def is_StrongNumber(self, n):
        def factorial(num):
            if num == 0 or num == 1:
                return 1
            else:
                return num * factorial(num - 1)

        sum_of_factorials = 0
        temp = n
        while temp > 0:
            digit = temp % 10
            sum_of_factorials += factorial(digit)
            temp //= 10

        return 1 if sum_of_factorials == n else 0



if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_StrongNumber(n)
		print(ans)
