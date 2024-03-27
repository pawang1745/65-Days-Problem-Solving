class Solution:
    def longest(self, arr, n):
        product = 1
        for num in arr:
            product *= num
        return product
        

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.longest(arr, n))

        T -= 1


if __name__ == "__main__":
    main()

