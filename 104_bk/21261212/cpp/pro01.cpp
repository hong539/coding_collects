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

*/

#include <stdio.h>
void main()
{
	int arr[]={1,2,3,4,5};
	int *ptr=arr;
	*(ptr++)+=1;
}