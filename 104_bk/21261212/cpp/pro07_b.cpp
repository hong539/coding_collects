/*
What’s the difference between a stack and a heap? How is memory allocated on the stack and heap? How do threads interact with the stack and the heap?

Ans:

gcc --version

gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Under My Ubuntu 22.04.3 LTS VM, execute "gcc -o pro07 pro07.cpp" to test codes.

Memory allocation on stack and heap:
In this example, we have a function foo that allocates an integer variable x on the stack and an integer pointer y on the heap using the new operator. 
We then print the values of x and y on the console. 
Finally, we deallocate the memory allocated on the heap using the delete operator.

*/

#include <iostream>

void foo() {
    int x = 5; // allocated on the stack
    int* y = new int(10); // allocated on the heap
    std::cout << "x: " << x << std::endl;
    std::cout << "y: " << *y << std::endl;
    delete y; // deallocate memory on the heap
}

int main() {
    foo();
    return 0;
}