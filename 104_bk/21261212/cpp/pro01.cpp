/*
Please see below code and answer questions
#include <stdio.h>
void main()
{
	int arr[]={1,2,3,4,5};
	int *ptr=arr;
	*(ptr++)+=1;
}
(1) What is the result of *ptr?
(2) What is the result of *(++ptr)?
(3) What is the result of arr array?

Ans:
good tips/guides from here : "https://hackmd.io/@sysprog/c-pointer#void--%E4%B9%8B%E8%AC%8E"

compiler explorer : "https://godbolt.org/"

gcc --version

gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Under My Ubuntu 22.04.3 LTS VM, when execute "gcc pro01.cpp" without specifying a standard using the "-std"
Show me this error message:

pro01.cpp:19:1: error: ‘::main’ must return ‘int’
   19 | void main()
      | ^~~~

So we have to fix the codes "void main()"

And I have to check out the default cpp std settings of gcc
g++ -x c++ -E -dM - < /dev/null | grep __cplusplus

#define __cplusplus 201703L

C++17?

#cpp std info
199711L for C++98
201103L for C++11
201402L for C++14
201703L for C++17

test codes with gcc
gcc -o pro01 pro01.cpp 
*/

#include <stdio.h>
int main()
{
	int arr[]={1,2,3,4,5};
	int *ptr=arr;
	//Calculate length of array
	int length = sizeof(arr)/sizeof(arr[0]);
	printf("Elements of given array arr: \n");
	for (int i = 0; i < length; i ++){
		printf("%d ", arr[i]);
	}
	printf("\n");
	printf("Before doing this operation \"*(ptr++)+=1\", \n now \"*ptr\" is: %d \n", *ptr);
	*(ptr++)+=1;
	printf("After doing this operation \"*(ptr++)+=1\", \n we have \"*ptr\" is: %d \n", *ptr);
	printf("I don't know where is the code \"*(++ptr)\" so I can not get the results. :( \n");
	printf("Elements of given array arr after operation \"*(ptr++)+=1\": \n");
	for (int i = 0; i < length; i ++){
		printf("%d ", arr[i]);
	}
	printf("\n");
}