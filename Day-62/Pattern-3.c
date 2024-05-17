// Aabcde
// ABabcd
// ABCabc
// ABCDab
// ABCDEa
#include <stdio.h>
int main() {
    int n = 5;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i + 1; j++) {
            printf("%c", j + 65);
        }
        for (int j = 0; j < n - i; j++) {
            printf("%c", j + 97);
        }
        printf("\n");
    }
    return 0;
}
