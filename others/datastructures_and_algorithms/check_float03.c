#include <stdio.h>
int main() {
    // IEEE754 調整
    // 浮點數的標準?
    float sum = 0.0f, corr = 0.0f; /* corrective value for rounding error */
    for (int i = 0; i < 10000; i++) {
        float y = (i + 1) - corr; /* add the correction to specific item */
        float t = sum + y; /* bits might be lost */
        corr = (t - sum) - y; /* recover lost bits */
        sum = t;
    }
    printf("Sum: %f\n", sum);
    return 0;
}