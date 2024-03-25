
class Solution:
    def count_divisors(self, N):
        count = 0
        for i in range(1, int(N**0.5) + 1):
            if N % i == 0:
                if i % 3 == 0:
                    count += 1
                if i != N // i and (N // i) % 3 == 0:
                    count += 1
        return count


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.count_divisors(N))
