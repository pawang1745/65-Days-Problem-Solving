class Solution:
    def divisibleBy11(self, S):
        # Initialize the sum
        sum_even = 0
        sum_odd = 0
        
        # Iterate over each digit in the number
        for i in range(len(S)):
            if i % 2 == 0:
                sum_even += int(S[i])  # Add digit at even position to sum_even
            else:
                sum_odd += int(S[i])   # Add digit at odd position to sum_odd
        
        # Calculate the difference
        difference = abs(sum_even - sum_odd)
        
        # Check if the difference is divisible by 11
        if difference % 11 == 0:
            return 1  # Divisible by 11
        else:
            return 0  # Not divisible by 11


if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		s = input ()
		ob = Solution()
		print (ob.divisibleBy11 (s)) 

