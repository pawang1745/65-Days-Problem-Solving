// using loop
#include <stdio.h>
int main() {
    int i=0, n=10,sum=0;
    while(i<=n){
        sum+=i*i;
        i++;
    }
    printf("%d",sum);
    return 0;
}

// using formula - (n*(n+1) + 2*(n+1)/6)

#include <stdio.h>
int main() {
    int  n=10,sum=0;
    sum=(n*(n+1) *( 2*n+1)/6);
    printf("%d",sum);
    return 0;
}
