#include<stdio.h>
int main(){
    int arr[4]={1,29,4,8};
    int sum=0;
    for(int i=0;i<4;i++){
        sum+=arr[i];
    }
    printf("%d",sum);
    return 0;
}
