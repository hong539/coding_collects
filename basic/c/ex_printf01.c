#include <stdio.h>

//格式字串
//printf可以輸出的字串可以用類似跳脫字元的方式，放置一些格式符
// %d, %i, %u, %o, %o, %x

int main(int argc, char const *argv[])
{
    /* code */
    int a = 123456789;              //123456789
    unsigned int b = 3000000000;    //-1294967296
    printf("%d\n", a);
    printf("%d\n", b);

    printf("%u\n", b);              //3000000000
    printf("%u\n", a);              //123456789
    // printf("Hello world!");    
    return 0;
}
