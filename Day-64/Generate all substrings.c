#include <stdio.h>
#include <string.h>
void generateSubstrings(char str[]) {
    int len = strlen(str);
    for (int start = 0; start < len; start++) {
        for (int end = start; end < len; end++) {
            for (int i = start; i <= end; i++) {
                printf("%c", str[i]);
            }
            printf("\n");
        }
    }
}
int main() {
    char str[100];
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    size_t len = strlen(str);
    if (len > 0 && str[len - 1] == '\n') {
        str[len - 1] = '\0';
    }
    printf("All substrings of \"%s\" are:\n", str);
    generateSubstrings(str);
    return 0;
}
