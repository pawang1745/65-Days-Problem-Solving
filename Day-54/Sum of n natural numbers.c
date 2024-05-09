//using loop

#include <stdio.h>
int main() {
    int i=0, n=10,sum=0;
    while(i<=n){
        sum+=i;
        i++;
    }
    printf("%d",sum);
    return 0;
}

//using formula

#include <stdio.h>
int main() {
    int  n=10,sum=0;
    sum=n*(n+1)/2;
    printf("%d",sum);
    return 0;
}
