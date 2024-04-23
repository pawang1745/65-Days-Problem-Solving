class Solution:
    def solve(self, n, d):
        result = []
        for i in range(n + 1):
            if str(d) in str(i):
                result.append(i)
        if not result:  # If result is empty
            return [-1]  # Return [-1] as per the problem statement
        return result


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n, d = [int(x) for x in input().split()]

        solObj = Solution()

        ans = solObj.solve(n, d)
        
        for e in ans:
            print(e,end = ' ')
        print()
