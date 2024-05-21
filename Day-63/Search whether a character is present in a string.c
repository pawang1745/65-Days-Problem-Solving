#include<stdio.h>
int main(){
    int n=100;
    char str[n];
    scanf("%s",str);
    int i;
    char trgt='N' ;
    int flag=0;
    for(i=0;i<n;i++){
        if(str[i]==trgt){
            flag=1;
            break;
        }
    }
    if(flag==1){
        printf("found");
    }
    else{
        printf("not found");
    }
    return 0;
}
