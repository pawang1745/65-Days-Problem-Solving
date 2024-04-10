class Solution:
    def getAngle(self, H, M):
        # Calculate the hour hand position
        hour_angle = (H % 12) * 30 + M / 2
        
        # Calculate the minute hand position
        minute_angle = M * 6
        
        # Calculate the difference between the angles
        angle = abs(hour_angle - minute_angle)
        
        # Since there can be two angles, take the minimum angle
        angle = min(angle, 360 - angle)
        
        # Return the floor of the final result angle
        return int(angle)


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        H,M=map(int,input().split())
        
        ob = Solution()
        print(ob.getAngle(H,M))
