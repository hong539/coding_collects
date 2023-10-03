/*
	What’s the difference between a stack and a heap? How is memory deallocated on the stack and heap? How do threads interact with the stack and the heap?
Ans:

src: https://www.shekhali.com/stack-vs-heap-understanding-the-difference-between-stack-and-heap-memory-in-c-sharp/

C# Stack Example

*/

using System;
using System.Collections;
namespace StackExample
{
    class Program
    {
        public static void Main(string[] args)
        {
            // Creating and initializing a new Stack.
            Stack stack = new Stack();
            stack.Push(1);
            stack.Push(2);
            stack.Push(3);
            stack.Push(4);
  
            // Reading elements from the stack
            foreach(var item in stack)
            {
                Console.Write($"{item} ,");
            }          
            Console.ReadLine();          
        }
        // Output: 4, 3, 2, 1,
    }
}