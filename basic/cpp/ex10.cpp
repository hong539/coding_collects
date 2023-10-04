#include <iostream>
using namespace std;

int main(){
    const int myNum = 15;
    //myNum = 10;
    /*error: assignment of read-only variable ‘myNum’
    6 |     myNum = 10;
    */
    cout << myNum << "\n";
    const int minutesPerHour = 60;
    const float PI = 3.14;
    cout << minutesPerHour << "\n" << PI << "\n";
    return 0;
}