#include <stdio.h>
int main() {
    float sum = 0.0f;
    for (int i = 0; i < 10000; i++) sum += i + 1;
    printf("Sum: %f\n", sum);
    return 0;
}