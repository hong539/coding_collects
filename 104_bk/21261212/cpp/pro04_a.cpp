/*
Please explain the (1) meaning & benefit of virtual function (2) benefit of virtual destructor

Ans:

gcc --version

gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Under My Ubuntu 22.04.3 LTS VM, execute "gcc -o pro04 pro04.cpp" to test codes.

A virtual function is a function that is declared in a base class and redefined in a derived class. 
When you call a virtual function on an object, the actual function that gets executed depends on the type of the object, not the type of the pointer or reference used to call the function. 
The main benefit of using virtual functions is that they allow you to achieve polymorphism in C++. Polymorphism is the ability of objects of different classes to be treated as if they were objects of the same class. 
This can be useful when you have a collection of objects of different types, but you want to perform some operation on all of them in a uniform way.

A virtual destructor is a destructor that is declared as virtual in a base class. 
When you delete an object through a pointer to its base class, and the base class has a virtual destructor, then the destructor of the derived class will be called first, followed by the destructor of the base class 13. This is important when you have a hierarchy of classes with destructors that need to release resources allocated by their respective constructors. 
If you don’t declare the destructor as virtual, then only the destructor of the base class will be called, which can lead to memory leaks and other problems.

*/
//Virtual function
#include <iostream>

class Shape {
public:
    virtual void draw() {
        std::cout << "Drawing a shape." << std::endl;
    }
};

class Circle : public Shape {
public:
    void draw() override {
        std::cout << "Drawing a circle." << std::endl;
    }
};

int main() {
    Shape* s = new Circle();
    s->draw(); // Output: Drawing a circle.
    delete s;
    return 0;
}