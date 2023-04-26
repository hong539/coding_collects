#include <stdint.h>
int32_t abs(int32_t x) {
    int32_t mask = (x >> 31);
    return (x + mask) ^ mask;
}

// abs(-2147483648)?