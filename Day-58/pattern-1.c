// *#*#*
// *#*#
// *#*
// *#
// *
#include<stdio.h>
int main(){
    int n,i,j;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        for(j=n;j>i;j--){
            if(j%2==0){
                printf("#");
            }
            else{
                printf("*");
            }
        }
        printf("\n");
    }
}
