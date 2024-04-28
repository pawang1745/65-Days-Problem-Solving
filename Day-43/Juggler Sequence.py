class Solution:
    def jugglerSequence(self, n):
        sequence = [n]
        
        while n != 1:
            if n % 2 == 0:
                n = int(n ** 0.5)
            else:
                n = int(n ** 1.5)
            sequence.append(n)
        
        return sequence



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        arr = ob.jugglerSequence(n)
        for i in (arr):
            print(i, end=" ")
        print()
