class Solution:
    def gfSeries(self, N: int) -> None:
        # Initialize the first two terms
        T0 = 0
        T1 = 1
        
        # Print the first two terms
        print(T0, T1, end=" ")
        
        # Generate the remaining terms
        for _ in range(2, N):
            Tn = T0**2 - T1
            print(Tn, end=" ")
            
            # Update the previous terms for the next iteration
            T0, T1 = T1, Tn
        
        # Print newline character after each testcase
        print()
        
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        obj = Solution()
        obj.gfSeries(N)
