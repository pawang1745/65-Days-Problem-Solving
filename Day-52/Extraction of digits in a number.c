#include <stdio.h>

int main() {
    int num,r;
    printf("enter a number: ");
    scanf("%d",&num);
    while(num!=0){
        r=num%10;
        printf("%d\n",r);
        num/=10;
    }

    return 0;
}
