#include <stdio.h>
int main() {
    int start=0,end=10;
    printf("Even\n");
    for(int i=start;i<=end;i++){
        if(i%2==0)
        printf("%d",i);
    }
    printf("\n");
    printf("Odd\n");
    for(int i=start;i<=end;i++){
        if(i%2==1)
        printf("%d",i);
    }    

    return 0;
}
