class Solution:
    def simpleInterest(self,A,B,C):
        #code here
        a=(A*B*C)/100
        return a


if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        P,R,T=map(int,input().strip().split(' '))
        ob=Solution()
        print('%.2f'%ob.simpleInterest(P,R,T))
