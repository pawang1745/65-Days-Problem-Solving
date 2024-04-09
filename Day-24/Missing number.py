from typing import List

class Solution:
    def missingNumber(self, n: int, arr: List[int]) -> int:
        # Calculate the sum of numbers from 1 to n
        total_sum = n * (n + 1) // 2
        
        # Calculate the sum of elements in the array
        array_sum = sum(arr)
        
        # The missing number is the difference between the total sum and the sum of elements in the array
        return total_sum - array_sum
        
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n-1)
        
        obj = Solution()
        res = obj.missingNumber(n, arr)
        
        print(res)
