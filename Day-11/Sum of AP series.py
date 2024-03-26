class Solution:
    def sum_of_ap(self, n, a, d):
        # Calculate the sum of the arithmetic progression
        sum_ap = (n / 2) * (2 * a + (n - 1) * d)
        return int(sum_ap)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, a, d = input().split()
		n = int(n)
		a = int(a)
		d = int(d)
		ob = Solution();
		ans = ob.sum_of_ap(n, a, d)
		print(ans)
