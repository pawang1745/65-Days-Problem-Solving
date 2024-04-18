class Solution:
    def modify(self, N):
        # Convert N to a string
        N = str(N)
        
        # Initialize an empty string to store the modified integer
        modified_N = ""
        
        # Iterate through the digits of the input string
        for i in range(len(N)):
            # If the current digit is not equal to the next one, append it to the modified string
            if i == len(N) - 1 or N[i] != N[i+1]:
                modified_N += N[i]
        
        return modified_N


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        num = int(input())

        solObj = Solution()

        print(solObj.modify(num))
