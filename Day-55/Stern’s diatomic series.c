#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);
    int a=1,b=n;
    for(int i=0;i<n;i++){
        
        printf("%d %d ",a,b);
        a+=1;
        b-=1;
    }
    return 0;
}
