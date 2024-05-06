class Solution:
    def sumOfFifthPowers(self, N):
        # Calculate the sum of the fifth powers
        sum_of_fifth_powers = 0
        for i in range(1, N + 1):
            sum_of_fifth_powers += i**5
        
        return sum_of_fifth_powers



if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfFifthPowers(N))
