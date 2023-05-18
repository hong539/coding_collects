#include <stdio.h>

//test
// Please enter the first integer: 4
// Please enter the second integer: 4
// Please enter the third integer: 3
// Average: 3

//test
// Please enter the first integer: 3
// Please enter the second integer: 3
// Please enter the third integer: 4
// Average: 3.000000

int main(int argc, char const *argv[])
{
    int num1, num2 , num3;
    printf("Please enter the first integer: ");
    scanf("%d", &num1);
    printf("Please enter the second integer: ");
    scanf("%d", &num2);
    printf("Please enter the third integer: ");
    scanf("%d", &num3);
    // 3. -> double
    double average = (num1 + num2 +num3) / 3.;
    printf("Average: %f\n", average);
    return 0;
}
