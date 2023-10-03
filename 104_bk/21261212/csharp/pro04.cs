/*
	Please consider the following code.

namespace ConsoleApplication1
{
    public delegate TResult Func<T, TResult>(T arg);
    class Program
    {
        static void Main(string[] args)
        {
            Func<string, int> returnLength;
            returnLength = delegate(string text) { return text.Length; };
            Console.WriteLine(returnLength("abc"));
        }
    }
}

Please rewrite it in C# Lambda expression.

Ans:

*/

namespace ConsoleApplication1
{
    public delegate TResult Func<T, TResult>(T arg);
    class Program
    {
        static void Main(string[] args)
        {
            Func<string, int> returnLength;
            returnLength = delegate(string text) { return text.Length; };
            Console.WriteLine(returnLength("abc"));
        }
    }
}