#include <stdio.h>
#include <math.h>
#include<stdlib>


int isAutomorphic(int num) {
  if (num < 0) {
    num = abs(num);
  }

  int count = floor(log10(abs(num))) + 1;

  int square = num * num;
  int last_digits = square % (int)pow(10, count);

  return num == last_digits;
}

int main() {
  int number;

  printf("Enter a number: ");
  scanf("%d", &number);

  if (isAutomorphic(number)) {
    printf("%d is an automorphic number.\n", number);
  } else {
    printf("%d is not an automorphic number.\n", number);
  }

  return 0;
}
