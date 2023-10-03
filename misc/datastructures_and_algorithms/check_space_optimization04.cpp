// https://www.geeksforgeeks.org/space-optimization-using-bit-manipulations/
// C++ program to mark numbers as multiple of 2 or 5
#include <bits/stdc++.h>
using namespace std;

// Driver code
int main()
{
	int a = 2, b = 10;
	int size = abs(b - a) + 1;
	int* array = new int[size];

	// Iterate through a to b, If it is a multiple
	// of 2 or 5 Mark index in array as 1
	for (int i = a; i <= b; i++)
		if (i % 2 == 0 || i % 5 == 0)
			array[i - a] = 1;

	cout << "MULTIPLES of 2 and 5:\n";
	for (int i = a; i <= b; i++)
		if (array[i - a] == 1)
			cout << i << " ";

	return 0;
}