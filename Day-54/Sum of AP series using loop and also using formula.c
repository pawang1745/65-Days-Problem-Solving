//using loop
#include <stdio.h>
int main() {
    int a=4,d=2,n=10,i=0,sum=0;
    while(i<n){
        sum+=a;
        a+=d;
        i++;
    }
    printf("%d",sum);
    return 0;
}




//using formula - (n(2*a+(n-1)*d)//2)

#include <stdio.h>
int main() {
    int a=4,d=2,n=10,sum=0;
    sum=(n*(2*a+(n-1)*d)/2);
    printf("%d",sum);
    return 0;
}
