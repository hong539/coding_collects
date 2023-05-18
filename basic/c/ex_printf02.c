#include <stdio.h>

int main(int argc, char const *argv[])
{
    float a = 123.45;
    double b = 123.45;
    printf("%f\n", a);      //123.449997
    printf("%f\n", b);      //123.450000

    printf("%d\n", a);
    printf("%d\n", b);
    return 0;
}
