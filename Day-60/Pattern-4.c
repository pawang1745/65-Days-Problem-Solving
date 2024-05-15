// 1        1
// 12      21
// 123    321
// 1234  4321
// 1234554321
#include <stdio.h>
int main() {
    int n = 5; // Number of rows
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = 1; j <= i + 1; j++) {
            printf("%d", j);
        }
        for (j = 0; j < 2 * (n - i - 1); j++) {
            printf(" ");
        }
        for (j = i + 1; j > 0; j--) {
            printf("%d", j);
        }
        printf("\n");
    }
    return 0;
}

