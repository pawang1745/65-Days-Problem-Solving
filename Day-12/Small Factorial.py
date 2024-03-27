import math
class Solution:
	def find_fact(self, n):
		# Code here
		if n==0:
		    return 1
		else:
		    return n*math.factorial(n-1)


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.find_fact(n)
		print(ans)
