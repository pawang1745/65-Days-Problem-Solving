class Solution:
	def find(self, l, b, h):
		# Code here
		surface_area=(2*((b*h)+(h*l)+(l*b)))
		volume=l*b*h
		return surface_area, volume

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		l, b, h = input().split()
		l = int(l); b = int(b); h = int(h);
		ob = Solution()
		ans = ob.find(l, b, h)
		for _ in ans:
			print(_, end = " ")
		print()
