/*
	Which of the following is the correct way to call the function MyFun() of the Sampleclass given below?

class Sample
{
    public int MyFun(int i)
    {
        Console.WriteLine("Welcome to Kway Kernel Team!" );
        return 0;
    }
}

(a)
	delegate void del(int i);
	Sample s = new Sample();
	deld = new del(ref s.MyFun);
	d(10);
(b)
	delegate int del(int i);
	Sample s = new Sample(.);
	del = new delegate(ref MyFun);
	del(10);
(c)
	Sample s = new Sample();
	delegate void del = new delegate(ref MyFun);
	del(10);
(d)
	delegate int del(int i);
	del d;
	Sample s = new Sample();
	d = new del(ref s.MyFun);
	d(10);

Ans:

*/

class Sample
{
    public int MyFun(int i)
    {
        Console.WriteLine("Welcome to Kway Kernel Team!" );
        return 0;
    }
}