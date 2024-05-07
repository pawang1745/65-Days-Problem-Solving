#include <stdio.h>

int main() {
    int num,r,sum=0,cpy;
    printf("enter a number: ");
    scanf("%d",&num);
    cpy=num;
    while(cpy!=0){
        r=cpy%10;
        sum+=r*r*r;
        cpy/=10;
    }
    if(num==sum){
        printf("Armstrong number");
    }
    else{
        printf("Not a Armstrong number");
    }
    
    return 0;
}
