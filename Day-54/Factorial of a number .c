#include <stdio.h>
int main() {
    int i=1, n=5,fact=1;
    while(i<=n){
        fact*=i;
        i++;
    }
    printf("%d",fact);
    return 0;
}
