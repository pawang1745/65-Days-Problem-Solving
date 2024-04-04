class Solution:
    def find(self, A, B):
  # Calculate the dot product of A and B
        dot_product = A[0] * B[0] + A[1] * B[1] + A[2] * B[2]
  
  # Calculate the magnitude squared of the cross product of A and B
        magnitude_squared_cross_product = (A[1] * B[2] - A[2] * B[1])**2 + (A[0] * B[2] - A[2] * B[0])**2 + (A[0] * B[1] - A[1] * B[0])**2
  
  # Check for parallel vectors
        if magnitude_squared_cross_product == 0:
            return 1
  # Check for perpendicular vectors  
        elif dot_product == 0:
            return 2
  # Otherwise, neither parallel nor perpendicular
        else:
            return 0


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = list(map(int, input().split()))
		B = list(map(int,input().split()))
		ob = Solution()
		ans = ob.find(A, B)
		print(ans)
