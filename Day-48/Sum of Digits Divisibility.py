class Solution:
    def isDivisible(self, N):
        # Calculate the sum of digits
        digit_sum = sum(int(digit) for digit in str(N))
        
        # Check if N is divisible by the sum of its digits
        if N % digit_sum == 0:
            return 1
        else:
            return 0



if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDivisible(N))
