#include <stdio.h>
#include <dlfcn.h>

int main() {
    void* handle = dlopen("libmy_program.so", RTLD_LAZY);
    if (!handle) {
        fprintf(stderr, "%s\n", dlerror());
        return 1;
    }

    int (*add_numbers)(int, int) = dlsym(handle, "add_numbers");
    if (!add_numbers) {
        fprintf(stderr, "%s\n", dlerror());
        return 1;
    }

    int result = add_numbers(3, 4);
    printf("Result: %d\n", result);

    dlclose(handle);
    return 0;
}