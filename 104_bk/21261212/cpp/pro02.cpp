/*
What is the output of this program?
   #include <iostream>
   using namespace std;
   class X
   {
      public:
      int a;
	 void f(int b) {
		cout<< b << endl; }
   };
   int main()
   {
       int X::*ptiptr = &X::a;
       void (X::*ptfptr)(int) = &X::f;
       X xobject;
       xobject.*ptiptr = 10;
       cout << xobject.*ptiptr << endl;
       (xobject.*ptfptr) (20);
   }

Ans:

*/