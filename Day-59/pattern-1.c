// 1 
// 3 3 
// 5 5 5 
// 7 7 7 7 
// 9 9 9 9 9
#include <stdio.h>
int main() {
    int rows ;
    scanf("%d",&rows);
    int i, j;
    for(i = 1; i <= rows; i++) {
        for(j = 1; j <= i; j++) {
            printf("%d ", 2 * i - 1);
        }
        printf("\n");
    }
    return 0;
}
