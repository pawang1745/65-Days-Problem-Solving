class Solution:
    def middle(self,A,B,C):
        #code here
        smaller = min(A, B)
        larger = max(A, B)
        
        # Comparing C with the larger of A and B
        if smaller < C < larger:
            return C
        elif C < smaller:
            return smaller
        else:
            return larger
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split())
        ob=Solution()
        print(ob.middle(A,B,C))
