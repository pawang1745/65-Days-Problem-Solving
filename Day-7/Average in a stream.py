class Solution:
	def streamAvg(self, arr, n):
		# code here
		averages = []
        sum = 0
        for num in arr:
            sum += num
            avg = sum / (len(averages) + 1)
            averages.append(avg)
            
        return averages

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.streamAvg(arr, n)
        for x in ans:
            print('%.2f'%x, end=" ")
        print()
        tc -= 1
