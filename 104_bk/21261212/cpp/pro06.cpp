/*
Given an array A[1~n], please write code to find the smallest and largest element with function template form efficiently.
What is the complexity (BigO) of your implementation?
[Note] The basic algorithm use O(2n) comparison.

Ans:

gcc --version

gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Under My Ubuntu 22.04.3 LTS VM, execute "gcc -o pro06 pro06.cpp" to test codes.

The function find_min_max takes an array A of type T, its size n, and two references to variables of type T to store the minimum and maximum elements. 
It initializes the minimum and maximum elements to the first element of the array and then iterates over the remaining elements to update the minimum and maximum values. 
The function template has a time complexity of O(n) 1.

In the main function, we create an integer array A with some values and call the find_min_max function to find its smallest and largest elements. 
The output is then printed on the console.

*/

#include <iostream>
#include <algorithm>

template <typename T>
void find_min_max(T* A, int n, T& min, T& max) {
    min = max = A[0];
    for (int i = 1; i < n; ++i) {
        if (A[i] > max) {
            max = A[i];
        }
        if (A[i] < min) {
            min = A[i];
        }
    }
}

int main() {
    int A[] = {1, 2, 3, 4, 5};
    int n = sizeof(A) / sizeof(A[0]);
    int min, max;
    find_min_max(A, n, min, max);
    std::cout << "Smallest element: " << min << std::endl;
    std::cout << "Largest element: " << max << std::endl;
    return 0;
}
