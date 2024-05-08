#include<stdio.h>

int max(int a, int b) {
  return (a > b) ? a : b;
}

int min(int a, int b) {
  return (a < b) ? a : b;
}

int main(){
    int a,b;
    scanf("%d %d",&a,&b);
    printf("Maximum: %d", max(a,b));
    printf("Minimum: %d", min(a,b));
    return 0;
}
