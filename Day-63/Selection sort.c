#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    for(int i=0;i<n;i++){
        int index=i;
        for(int j=i+1;j<n;j++){
            if(arr[j]<arr[i]){
                index=j;
            }
        }
        int temp=arr[i];
        arr[i]=arr[index];
        arr[index]=temp;
    }
    for(int k=0;k<n;k++){
        printf("%d",arr[k]);
    }
    return 0;
}
