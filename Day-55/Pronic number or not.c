#include <stdio.h>

int main() {
    int n,first=0,second=1,flag=0;
    scanf("%d",&n);
    while(first*second<=n){
        if(first*second==n){
            flag=1;
            break;
        }
        first+=1;
        second+=1;
    }
    if(flag==0){
        printf("Not pronic");
    }
    else{
        printf("Pronic");
    }
    return 0;
}
