class Solution:
    def getNumber(self, B, N):
        # Initialize an empty list to store digits
        result = []

        # Define hexadecimal digits for bases greater than 10
        digits = "0123456789ABCDEF"

        # Edge case: if N is 0, just return "0"
        if N == 0:
            return "0"

        # Convert decimal number N to base B
        while N > 0:
            # Calculate remainder when dividing N by B
            remainder = N % B
            # Append remainder to result list
            result.append(digits[remainder])
            # Update N to quotient of N divided by B
            N //= B

        # Reverse the list to get correct order
        result.reverse()

        # Convert list of digits to string and return
        return "".join(result)


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        B = int(input())
        N = int(input())
        ob = Solution()
        ans = ob.getNumber(B, N)
        print(ans)
