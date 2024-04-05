class Solution:    
    # Function to return the count of number of elements in union of two arrays.
    def doUnion(self, a, n, b, m):
        # Initialize an empty set to store unique elements
        union_set = set()
        
        # Add elements of array a[] to the set
        for i in range(n):
            union_set.add(a[i])
        
        # Add elements of array b[] to the set
        for i in range(m):
            union_set.add(b[i])
        
        # Return the length of the set, which represents the count of elements in the union
        return len(union_set)


#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
