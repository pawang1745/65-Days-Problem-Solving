#include<stdio.h>
#include<math.h>
int main(){
    int num,rev=0,rem;
    scanf("%d",&num);
    while(num!=0){
        rem=num%10;
        rev=rev*10+rem;
        num/=10;
    }
    printf("%d",rev);
    return 0;
}
