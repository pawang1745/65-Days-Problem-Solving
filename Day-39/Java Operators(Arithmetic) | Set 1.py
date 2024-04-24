import math

class Solution:
    def FindRoots(self, A, B, C):
        # Calculate the discriminant
        discriminant = B*B - 4*A*C
        
        # If discriminant is negative, roots are not real
        if discriminant < 0:
            return [-1]
        
        # Calculate the roots
        sqrt_discriminant = math.sqrt(discriminant)
        root1 = (-B + sqrt_discriminant) / (2*A)
        root2 = (-B - sqrt_discriminant) / (2*A)
        
        # Return roots in ascending order
        return sorted([root1, root2])


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A, B, C = input().split()
		A = int(A); B = int(B); C = int(C);
		ob = Solution()
		ans = ob.FindRoots(A, B, C)
		if(len(ans) == 1):
			print(int(ans[0]))
			continue 
		for _ in ans:
			print('%.6f'%_, end = " ")
		print()

