class Solution:
    def countNumberswith4(self, N):
        count = 0
        for num in range(1, N + 1):
            if '4' in str(num):
                count += 1
        return count


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countNumberswith4(N))
