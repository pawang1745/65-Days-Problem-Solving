#include <stdio.h>

int main() {
    int num,sum=0,cpy;
    printf("enter a number: ");
    scanf("%d",&num);
    cpy=num;
    while(cpy!=0){
        sum+=cpy%10;
        cpy/=10;
    }
    if(num%sum==0){
        printf("Harshad number");
    }
    else{
        printf("Not a harshad number");
    }
    
    return 0;
}
