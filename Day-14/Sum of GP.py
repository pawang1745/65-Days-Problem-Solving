
class Solution:
    def sum_of_gp(self, n, a, r):
        # Check if the common ratio is 1
        if r == 1:
            return n * a
        
        # Calculate the sum of the geometric progression series
        sum_series = a * ((r**n) - 1) // (r - 1)
        return sum_series


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, a, r = input().split()
		n = int(n)
		a = int(a)
		r = int(r)
		ob = Solution();
		ans = ob.sum_of_gp(n, a, r)
		print(ans)
