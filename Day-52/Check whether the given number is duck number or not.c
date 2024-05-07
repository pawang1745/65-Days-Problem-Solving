#include <stdio.h>
int main() {
    int num,r,flag=0;
    printf("enter a number: ");
    scanf("%d",&num);
    while(num!=0){
        r=num%10;
        if(r==0){
            flag=1;
            break;
        }
        num/=10;
        
    }
    if(flag==1){
        printf("Duck number");
    }
    else{
        printf("Not Duck number");
    }
    return 0;
}
