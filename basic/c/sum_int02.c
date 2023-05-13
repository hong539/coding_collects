#include <stdio.h>

// if I want to caculate sum of 100 intergers?
// usage of memory?
// Can we just use two variables?
int main() {
    int integer1, integer2, integer3, sum;
    printf("Please enter the first interger: ");
    scanf("%d", &integer1);
    printf("Please enter the second interger: ");
    scanf("%d", &integer2);
    printf("Please enter the third interger: ");
    scanf("%d", &integer3);    
    sum = integer1 + integer2 + integer3;
    printf("Sum is %d. \n", sum);
    return 0;
}