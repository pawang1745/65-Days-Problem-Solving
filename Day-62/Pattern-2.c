// P
// PA
// PAW
// PAWA
// PAWAN

#include <stdio.h>
#include <string.h>
int main() {
    char pattern[] = "PAWAN";
    int length = strlen(pattern);
    for (int i = 1; i <= length; i++) {
        for (int j = 0; j < i; j++) {
            printf("%c", pattern[j]);
        }
        printf("\n");
    }
    return 0;
}
