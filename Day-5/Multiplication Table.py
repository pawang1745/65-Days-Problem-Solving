class Solution:
    def getTable(self, N):
        arr = []
        for i in range(1, 11):
            arr.append(i * N)
        return arr




if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.getTable(N)
        for i in ans:
            print(i,end=" ")
        print()
