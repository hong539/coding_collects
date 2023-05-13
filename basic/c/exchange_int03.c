// integer1, integer2 -> 2, 6
// after exchange integer1, integer2 -> 6, 2
// C語言無法多重指定
// 整數的特性
#include <stdio.h>

int main() {
    int integer1, integer2;
    printf("Please enter the first interger: ");
    scanf("%d", &integer1);
    printf("Please enter the second interger: ");
    scanf("%d", &integer2);

    integer1 = integer1 ^ integer2;
    integer2 = integer1 ^ integer2;
    integer1 = integer1 ^ integer2;
    
    printf("integer1: %d\n", integer1);
    printf("integer2: %d\n", integer2);
    return 0;
}