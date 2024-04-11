class Solution:
    def maximizeMoney(self, N, K):
        if N == 0:
            return 0
        if N == 1:
            return K

        # Calculate the maximum money robbed starting from the first house
        max_money_from_first_house = (N + 1) // 2 * K

        # Calculate the maximum money robbed starting from the second house
        max_money_from_second_house = N // 2 * K

        # Return the maximum of the two
        return max(max_money_from_first_house, max_money_from_second_house)
 
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K = map(int,input().split())
        
        ob = Solution()
        print(ob.maximizeMoney(N,K))
