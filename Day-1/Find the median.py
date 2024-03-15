class Solution:
	def find_median(self, v):
	    v.sort()  # Sort the array in non-decreasing order
        n = len(v)
        if n % 2 == 0:  # If the number of elements is even
            return (v[n//2 - 1] + v[n//2]) // 2  # Average of two middle elements
        else:  # If the number of elements is odd
            return v[n//2]  # Middle element
		
		    




if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
