#include <assert.h>
int main() {
    // IEEE 754
    assert(0. == -0.);
    assert(1./0. == 1./-0.);
}