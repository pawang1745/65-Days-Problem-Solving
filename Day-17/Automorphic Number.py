class Solution:
    def is_AutomorphicNumber(self, n):
        square = n ** 2
        last_digit_n = n % 10
        last_digit_square = square % 10
        if last_digit_n == last_digit_square:
            return "Automorphic"
        else:
            return "Not Automorphic"



if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_AutomorphicNumber(n)
		print(ans)
