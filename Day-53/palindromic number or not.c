#include<stdio.h>
#include<math.h>
int main(){
    int num,rev=0,rem,org;
    scanf("%d",&num);
    org=num;
    while(num!=0){
        rem=num%10;
        rev=rev*10+rem;
        num/=10;
    }
    if(rev==org){
    printf("Palindrome");
    }
    else{
        printf("Not Palindrome");
    }
    return 0;
}
