class Solution:
    def kthDigit(self, A, B, K):
        # code here
         # Calculate A^B
        result = A ** B
    
    # Convert result to string
        result_str = str(result)
    
    # Find the Kth digit from right
        return result_str[-K]
        
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B,K = input().split()
        ob = Solution()
        print(ob.kthDigit(int(A),int(B),int(K)))
