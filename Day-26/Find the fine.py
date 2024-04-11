class Solution:
    def totalFine(self, n, date, car, fine):
        total_fine = 0
        
        # Check if the date is even
        is_even_date = date % 2 == 0
        
        # Iterate through the cars and fines
        for i in range(n):
            # Check if the car number is odd
            is_odd_car = car[i] % 2 != 0
            
            # Check if fine should be collected for this car
            if (is_even_date and is_odd_car) or (not is_even_date and not is_odd_car):
                total_fine += fine[i]
        
        return total_fine
    
def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        brr = [int(x) for x in input().strip().split()]
        
        print(Solution().totalFine( n, k, arr, brr))

        T -= 1


if __name__ == "__main__":
    main()

