class Solution:
    def isAmazing(self, n):
        # A function to count divisors
        def count_divisors(num):
            count = 0
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    # If both divisors are same, count only one
                    if num / i == i:
                        count += 1
                    else:
                        # Otherwise, count both
                        count += 2
            return count

        # Check if the number is a perfect square
        root = int(n ** 0.5)
        if root * root == n:
            # If the number is a perfect square, count its divisors
            div_count = count_divisors(n)
            # Check if it has exactly three divisors
            if div_count == 3:
                return 1
        return 0


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.isAmazing(n))
