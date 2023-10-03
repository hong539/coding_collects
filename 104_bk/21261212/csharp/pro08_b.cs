/*
	What’s the difference between a stack and a heap? How is memory deallocated on the stack and heap? How do threads interact with the stack and the heap?
Ans:

Heap

Heap memory is a region of memory that is dynamically allocated during a program’s runtime. Unlike stack memory, heap memory is not freed automatically, so it is the responsibility of the Garbage Collector (GC) or programmer to deallocate it once it is no longer needed manually.

This type of memory is used for storing global variables or objects that need to persist for the duration of the program.

The Heap memory can grow or shrink dynamically based on the program’s memory requirements.
The Garbage Collector (GC) is responsible for freeing heap memory by automatically managing and reclaiming a program’s memory that is no longer being used. It tracks which objects in a heap are still in use and frees the memory associated with unneeded objects, making it available for future use.

*/

int[] arr = new int[10];