#include <iostream>
using namespace std;
class Swap
{
private:
int a, b;
public:
// Constructor to initialize values
Swap(int x, int y)
{
a = x;
b = y;
}
// Friend function declaration
friend void swapValues(Swap &);
// Function to display the values
void display()
{
cout << "a = " << a << ", b = " << b << endl;
}
};
// Friend function definition
void swapValues(Swap &s)
{
int temp = s.a;
s.a = s.b;
s.b = temp;

}
int main()
{
// Create an object of class Swap
Swap obj(10, 40);
// Display values before swapping
cout << "Before swapping: ";
obj.display();
// Swap the values using the friend function
swapValues(obj);
// Display values after swapping
cout << "After swapping: ";
obj.display();
return 0;
}