#include <stdint.h>
int32_t abs(int32_t x) {
    int32_t mask = (x >> 31);
    return (x + mask) ^ mask;
}

// 取絕對值
// abs(-2147483648)?
// 解讀計算機編碼
// constant time?
// src: https://hackmd.io/@sysprog/binary-representation#%E6%95%B8%E5%80%BC%E8%A1%A8%E7%A4%BA%E7%9A%84%E6%9C%89%E6%95%88%E7%AF%84%E5%9C%8D