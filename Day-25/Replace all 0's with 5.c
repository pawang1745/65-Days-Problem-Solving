#include <stdio.h>

int convertFive(int n);


int main() {
    int T;
    scanf("%d",&T);
    while (T--) {
        int n;
        scanf("%d",&n);
        printf("%d\n",convertFive(n));
    }
}




//User function Template for C

int convertFive(int num) {
    int result = 0;
    int multiplier = 1; // To keep track of the place value

    while (num != 0) {
        int digit = num % 10; // Extract the last digit
        if (digit == 0) {
            // Replace 0 with 5
            result += 5 * multiplier;
        } else {
            // Keep the digit as it is
            result += digit * multiplier;
        }
        num /= 10; // Move to the next digit
        multiplier *= 10; // Update place value
    }

    return result;
}
