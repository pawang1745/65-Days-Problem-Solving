import math
class Solution:
	def findFocalLength(self, R, type):
		# Code here
		if type == "concave":
            return math.floor(R / 2)
        elif type == "convex":
            return math.floor(-R / 2)
        else:
            return "Invalid mirror type"


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		type = input()
		R = float(input())
		ob = Solution()
		ans = ob.findFocalLength(R, type)
		print(ans)
