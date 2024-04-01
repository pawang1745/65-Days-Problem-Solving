class Solution:
    def printFloydTriangle(self, N):
        num = 1
        for i in range(1, N + 1):
            for j in range(1, i + 1):
                print(num, end=" ")
                num += 1
            print()



if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printFloydTriangle(N)
