class Solution:
    def maximum_Cuts(self, n):
        return (n**2 + n + 2) // 2


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.maximum_Cuts(n)
		print(ans)
