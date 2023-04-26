// src01:https://www.geeksforgeeks.org/space-optimization-using-bit-manipulations/
// src02:https://docs.google.com/presentation/d/1xmb_mvsHISWp6naP1rHOyrxzMzNQkVoKK69lGRRXV9M/edit#slide=id.g1c01be6b518_0_17
// ask our ChatGPT XD
#include <stdio.h>

void print_multiples(int a, int b) {
    int start = (a + 1) / 2 * 2; // the first multiple of 2 >= a
    int end = b / 2 * 2; // the last multiple of 2 <= b
    int mask = 0; // the bit mask to mark the multiples
    
    // mark the multiples of 2
    for (int i = start; i <= end; i += 2) {
        mask |= (1 << (i % 32));
    }
    
    start = (a + 4) / 5 * 5; // the first multiple of 5 >= a
    end = b / 5 * 5; // the last multiple of 5 <= b
    
    // mark the multiples of 5
    for (int i = start; i <= end; i += 5) {
        mask |= (1 << (i % 32));
    }
    
    // print the marked multiples
    for (int i = a; i <= b; i++) {
        if (mask & (1 << (i % 32))) {
            printf("%d ", i);
        }
    }
}

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    print_multiples(a, b);
    return 0;
}