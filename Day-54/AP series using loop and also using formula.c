// using loop
#include <stdio.h>
int main() {
    int a=4,d=2,n=10,i=0;
    while(i<n){
        printf("%d ",a);
        a+=d;
        i++;
    }
    return 0;
}

// using formula
#include <stdio.h>
int main() {
    int a=4,d=2,n=10;
    int last= a+(n-1)*d;
    while(a<=last){
    printf("%d ",a);
    a+=d;
    }
    return 0;
}
