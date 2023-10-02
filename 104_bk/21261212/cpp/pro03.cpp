/*
Please write down the output of the following codes.
#include "stdafx.h"
#include <iostream>;
using namespace std;
class BaseObject {
public:
	BaseObject() { cout << "BaseObject constructor." << endl;}
	virtual ~BaseObject(){ cout << "BaseObject destructor." << endl;}
};
class DeriveObject : public BaseObject {
public:
	DeriveObject() { cout << "DeriveObject constructor." << endl;}
	~DeriveObject() { cout << "DeriveObject destructor." << endl;}
};
int _tmain(int argc, _TCHAR* argv[])
{
	DeriveObject testobject;
	return 0;
}

Ans:

gcc --version

gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Under My Ubuntu 22.04.3 LTS VM, execute "gcc -o pro03 pro03.cpp" to test codes.

Show me these messages:

pro03.cpp:35:10: fatal error: stdafx.h: No such file or directory
   35 | #include "stdafx.h"
      |          ^~~~~~~~~~
compilation terminated.

*/

#include "stdafx.h"
#include <iostream>;
using namespace std;
class BaseObject {
public:
	BaseObject() { cout << "BaseObject constructor." << endl;}
	virtual ~BaseObject(){ cout << "BaseObject destructor." << endl;}
};
class DeriveObject : public BaseObject {
public:
	DeriveObject() { cout << "DeriveObject constructor." << endl;}
	~DeriveObject() { cout << "DeriveObject destructor." << endl;}
};
int _tmain(int argc, _TCHAR* argv[])
{
	DeriveObject testobject;
	return 0;
}