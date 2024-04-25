class Solution:
    def checkPower(self, N):
        if N <= 1:
            return 1
        
        for x in range(2, int(N**0.5) + 1):
            y = 2
            power = x ** y
            while power <= N:
                if power == N:
                    return 1
                y += 1
                power = x ** y
                
        return 0


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())
        

        ob = Solution()
        print(ob.checkPower(N))
