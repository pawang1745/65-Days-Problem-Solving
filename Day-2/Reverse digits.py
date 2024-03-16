class Solution:
	def reverse_digit(self, n):
		# Code here
		num_str = str(n)
        
        # Reverse the string
        reversed_str = num_str[::-1]
        
        # Remove leading zeroes if any
        reversed_num = int(reversed_str.lstrip('0')) if reversed_str != '0' else 0
        
        return reversed_num




if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
