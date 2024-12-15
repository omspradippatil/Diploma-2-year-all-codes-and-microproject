#include<iostream>
using namespace std;

class Example {
public:
    int x;
    Example(int x) { this->x = x; }
    void show() { cout << "Value: " << x << endl; }

};

int main() {
    Example obj(10);
    obj.show();
    return 0;
}


