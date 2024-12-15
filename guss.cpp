#include<iostream>
using namespace std;
int main()
{
    
    int attemps=1;
    int random_number= rand() % 101;
    int gussed_no;
           

         
          
          
       do{
       
              cout << "guss the number between 0 to 100\n";
                cin >> gussed_no;

        if (gussed_no < random_number){
            cout << "guss again no. is greater\n ";
            cin >> gussed_no;
        }else{
             cout << "guss again no. is smaller\n ";
            cin >> gussed_no;
        }
         attemps++;
            
    }while(random_number != gussed_no);

     cout << "congralutions u gusssed the number right in :" << attemps<<"  attempts";

     return 0;

}