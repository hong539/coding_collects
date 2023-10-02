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

gcc --version

gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Under My Ubuntu 22.04.3 LTS VM, execute "gcc pro02.cpp -o pro02" to test codes.

Show me these messages:

/usr/bin/ld: /tmp/cctmkZLf.o: warning: relocation against `_ZSt4cout' in read-only section `.text._ZN1X1fEi[_ZN1X1fEi]'
/usr/bin/ld: /tmp/cctmkZLf.o: in function `main':
pro02.cpp:(.text+0x59): undefined reference to `std::cout'
/usr/bin/ld: pro02.cpp:(.text+0x61): undefined reference to `std::ostream::operator<<(int)'
/usr/bin/ld: pro02.cpp:(.text+0x68): undefined reference to `std::basic_ostream<char, std::char_traits<char> >& std::endl<char, std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&)'
/usr/bin/ld: pro02.cpp:(.text+0x73): undefined reference to `std::ostream::operator<<(std::ostream& (*)(std::ostream&))'
/usr/bin/ld: /tmp/cctmkZLf.o: in function `__static_initialization_and_destruction_0(int, int)':
pro02.cpp:(.text+0xda): undefined reference to `std::ios_base::Init::Init()'
/usr/bin/ld: pro02.cpp:(.text+0xf5): undefined reference to `std::ios_base::Init::~Init()'
/usr/bin/ld: /tmp/cctmkZLf.o: in function `X::f(int)':
pro02.cpp:(.text._ZN1X1fEi[_ZN1X1fEi]+0x1b): undefined reference to `std::cout'
/usr/bin/ld: pro02.cpp:(.text._ZN1X1fEi[_ZN1X1fEi]+0x23): undefined reference to `std::ostream::operator<<(int)'
/usr/bin/ld: pro02.cpp:(.text._ZN1X1fEi[_ZN1X1fEi]+0x2a): undefined reference to `std::basic_ostream<char, std::char_traits<char> >& std::endl<char, std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&)'
/usr/bin/ld: pro02.cpp:(.text._ZN1X1fEi[_ZN1X1fEi]+0x35): undefined reference to `std::ostream::operator<<(std::ostream& (*)(std::ostream&))'
/usr/bin/ld: warning: creating DT_TEXTREL in a PIE
collect2: error: ld returned 1 exit status

*/

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