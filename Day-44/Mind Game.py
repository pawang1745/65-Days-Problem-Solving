class Solution:
    def mindGame(self, K):
        # code here
        return K // 2


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        K=int(input())
        
        ob = Solution()
        print(ob.mindGame(K))
