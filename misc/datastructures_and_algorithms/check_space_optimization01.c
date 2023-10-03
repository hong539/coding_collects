// src01:https://www.geeksforgeeks.org/space-optimization-using-bit-manipulations/
// src02:https://docs.google.com/presentation/d/1xmb_mvsHISWp6naP1rHOyrxzMzNQkVoKK69lGRRXV9M/edit#slide=id.g1c01be6b518_0_17
#include <stdio.h>
#include <stdlib.h>
int main() {
    int a = 2, b = 10;
    int size = abs(b - a) + 1;
    int array[size];

    /* Iterate through a to b, If it’s a multiple of 2 or 5, mark index in array as 1 */
    for (int i = a; i <= b; i++)
        if (i % 2 == 0 || i % 5 == 0)
            array[i - a] = 1;
    for (int i = a; i <= b; i++)
        if (array[i - a] == 1)
            printf("%d ", i); 
    printf("\n");
    return 0;
}