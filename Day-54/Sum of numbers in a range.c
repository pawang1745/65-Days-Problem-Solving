// using loop

#include <stdio.h>
int main() {
    int i=4, n=10,sum=0;
    while(i<=n){
        sum+=i;
        i++;
    }
    printf("%d",sum);
    return 0;
}
 



// using formula

#include <stdio.h>
int main() {
    int  m=4,n=10,sum1=0,sum2=0;
    sum1=m*(m-1)/2;
    sum2=n*(n+1)/2;
    printf("%d",sum2-sum1);
    return 0;
}
