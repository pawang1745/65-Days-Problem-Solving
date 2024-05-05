class Solution:
    def celciusToFahrenheit(self, C):
        F = (9/5) * C + 32
        return round(F, 2)



if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print('%.2f'%ob.celciusToFahrenheit(N))
