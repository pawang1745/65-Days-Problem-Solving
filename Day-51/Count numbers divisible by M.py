class Solution:
    def countDivisibles (ob, A, B, M):
        # Count of numbers divisible by M from 1 to B
        count_B = B // M
        
        # Count of numbers divisible by M from 1 to A-1
        count_A_minus_1 = (A - 1) // M
        
        # Return the difference
        return count_B - count_A_minus_1


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A, B, M = input().split()
        A = int(A)
        B = int(B)
        M = int(M)
        
        ob = Solution()
        print(ob.countDivisibles(A, B, M))
