class Solution:
    def sumofproduct(self, n):
        total_sum = 0
        for x in range(1, n + 1):
            y = n // x
            total_sum += x * y
        return total_sum
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.sumofproduct(n)
		print(ans)
