class Solution:
    def EvenOdd(self, n1, n2):
        # code here
        product=n1*n2
        if product%2==0:
            return 1
        else:
            return 0



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a = int(input().strip())
        b = int(input().strip())
        ob = Solution()
        ans = ob.EvenOdd(a,b)
        print(ans)
