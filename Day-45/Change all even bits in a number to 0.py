class Solution:
    def convertEvenBitToZero(ob, n):
        mask = 0xAAAAAAAA  
        result = n & mask
        
        return result


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.convertEvenBitToZero(n))
