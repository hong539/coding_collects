/*
Please (1) explain the meaning of forward declaration (reduce dependency about header file) (2) Please rewrite the sample code with forward declaration.

//file C.h
#include "A.h"
#include "B.h"
class C 
{
    A* a;
    B b;
};

Ans:

gcc --version

gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Under My Ubuntu 22.04.3 LTS VM, execute "gcc -o pro05 pro05.cpp" to test codes.

*/

//file C.h
class A;
class B;
class C 
{
    A* a;
    B b;
};
