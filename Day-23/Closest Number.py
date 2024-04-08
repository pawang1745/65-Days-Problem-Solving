class Solution:
    def closestNumber(self, N, M):
        # Calculate remainder
        rem = abs(N) % abs(M)

        # Calculate two candidate numbers
        closest_lower = N - rem if N >= 0 else N + rem - abs(M)
        closest_upper = closest_lower + abs(M)

        # Check which one has the maximum absolute value
        if abs(N - closest_lower) <= abs(N - closest_upper):
            return closest_lower
        else:
            return closest_upper


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M=map(int,input().split())
        
        ob = Solution()
        print(ob.closestNumber(N,M))
