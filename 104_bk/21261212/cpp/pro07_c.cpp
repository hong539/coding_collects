/*
What’s the difference between a stack and a heap? How is memory allocated on the stack and heap? How do threads interact with the stack and the heap?

Ans:

gcc --version

gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Under My Ubuntu 22.04.3 LTS VM, execute "gcc -o pro07 pro07.cpp" to test codes.

Threads interaction with stack and heap:

In this example, we have a function foo that modifies an integer variable passed by reference. 
We then create a thread and pass a variable x by reference to it. The thread executes function foo, modifies variable x, and then terminates. 
We wait for the thread to finish using the join() method and then print the modified value of variable x.

*/

#include <iostream>
#include <thread>

void foo(int& x) {
    x += 5; // modify variable x
}

int main() {
    int x = 5; // allocated on the stack
    std::thread t(foo, std::ref(x)); // create a thread and pass variable x by reference
    t.join(); // wait for thread to finish
    std::cout << "x: " << x << std::endl; // print modified value of x
    return 0;
}