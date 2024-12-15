#include<iostream>
using namespace std;
class circle
        {
            float a,r;
            public:
            circle(float x)
             {
                r=x;
             }

            circle(circle&c) 
            {
                r=c.r;

            }
            void compute();
            void display();
        };
           inline void circle :: compute()
           {
            a=3.14*r*r;
           } 

           inline void circle :: display()
           {
              std::cout<<"area="<<a<<std::endl;
           }
int main()
{
     float p;
     cout<<"enter the radius of the circle";
     cin>>p;
     circle c(p);
     c.compute();
     c.display();
    //  circle c1(c);
    //  c1.compute();
    //  c1.display();


    return 0;
}

