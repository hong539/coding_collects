#include <stdio.h>

int main(int argc, char const *argv[])
{
    int num1, num2 , num3;
    printf("Please enter the first integer: ");
    scanf("%d", &num1);
    printf("Please enter the second integer: ");
    scanf("%d", &num2);
    printf("Please enter the third integer: ");
    scanf("%d", &num3);
    int average = (num1 + num2 +num3) / 3;
    printf("Average: %d\n", average);
    return 0;
}
