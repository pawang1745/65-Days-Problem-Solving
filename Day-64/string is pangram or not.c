#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define ALPHABET_SIZE 26 
int isPangram(char str[]) {
    int frequency[ALPHABET_SIZE] = {0};
    for (int i = 0; str[i]; i++) {
        char ch = tolower(str[i]); 
        if (ch >= 'a' && ch <= 'z') {
            frequency[ch - 'a']++;
        }
    }
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        if (frequency[i] == 0) {
            return 0; 
        }
    }
    return 1; 
}
int main() {
    char str[100];
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    size_t len = strlen(str);
    if (len > 0 && str[len - 1] == '\n') {
        str[len - 1] = '\0';
    }
    if (isPangram(str)) {
        printf("\"%s\" is a pangram.\n", str);
    } else {
        printf("\"%s\" is not a pangram.\n", str);
    }
    return 0;
}
