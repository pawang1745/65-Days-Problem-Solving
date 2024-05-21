#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    int i,j,k;
    for(i=0;i<n;i++){
        for(j=i;j<n;j++){
            for(k=i;k<j+1;k++){
                printf("%d",arr[k]);
            }
            printf("\n");
        }
    }
    return 0;
}
