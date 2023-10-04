#include <iostream>
using namespace std;

int main(){
    int x = 5, y = 6, z = 7;    
    cout << x + y + z;
    int x = y = z;
    x = y = z = 50;
    cout << x + y + z;
    return 0;
}