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

*/