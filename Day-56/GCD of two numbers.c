#include<stdio.h>
int main(){
    int n1,n2,div=1,res=1;
    scanf("%d %d",&n1,&n2);
    while(div<=n1 && div<=n2){
        if(n1%div==0 && n2%div==0){
            res=div;
            
        }
        div+=1;
    }
    printf("%d",res);
}
#include<stdio.h>
int main(){
    int n1,n2;
    scanf("%d %d",&n1,&n2);
    while(n2){
        n1=n2;
        n2=n1%n2;
    }
    printf("%d",n1);
}
