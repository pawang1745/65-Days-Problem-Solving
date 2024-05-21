#include <stdio.h>
#include<string.h>
int main(){
    char s[10];
    int vowel=0;
    fgets(s,sizeof s,stdin);
    for(int i=0;s[i]!='\0';i++)
    {
        if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'){
            vowel++;
        }
        
    }
    printf("vowel;%d",vowel);
}
