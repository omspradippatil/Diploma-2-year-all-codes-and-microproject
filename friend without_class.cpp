#include<iostream>
using namespace std;
class getdata
{
    public:
    int a,b,c;
public:

getdata(){
    cout << "i am a constructor\n";
}
    void dataget(){
        

        cout << "enter length and breadth\n";
        cin >> a >> b;

    }

    void putdata(){

        c=a*b;
        cout << " the area of rectangle is :"<<c<< endl;


    }

};

int main(){

    getdata data;
    data.dataget();
    data.putdata();


    return 0;
}