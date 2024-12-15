#include<iostream>
using namespace std;
class rectangle
{
    public:
    double l,b,answer;

    public:
    void getdata();
    void compute();
    void display();
};
inline void rectangle :: getdata()
{
    cout<< "enter the lenght and breadth of rectangle\n";
    cin>>l>>b;

}

inline void rectangle :: compute()
{
    answer=l*b;
}
inline void rectangle :: display()
{
    cout << "the area of rextangle is :"<<answer<<endl;
}

int main()
{
    rectangle r;
    r.getdata();
    r.compute();
    r.display();

    return 0;
}