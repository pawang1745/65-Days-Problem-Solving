// 1234554321
// 1234  4321
// 123    321
// 12      21
// 1        1
#include <stdio.h>
int main() {
    int n = 5; // Number of rows
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = 1; j <= n - i; j++) {
            printf("%d", j);
        }
        for (j = 0; j < 2 * i; j++) {
            printf(" ");
        }
        for (j = n - i; j > 0; j--) {
            printf("%d", j);
        }
        printf("\n");
    }
    return 0;
}
