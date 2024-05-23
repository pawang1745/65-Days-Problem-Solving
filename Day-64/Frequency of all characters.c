#include <stdio.h>
#include <string.h>
#define ASCII_SIZE 256 
void calculateFrequency(char str[]) {
    int frequency[ASCII_SIZE] = {0};
    for (int i = 0; i < strlen(str); i++) {
        frequency[(unsigned char)str[i]]++;
    }
    printf("Character frequencies:\n");
    for (int i = 0; i < ASCII_SIZE; i++) {
        if (frequency[i] > 0) {
            printf("'%c' : %d\n", i, frequency[i]);
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
    calculateFrequency(str);
    return 0;
}
