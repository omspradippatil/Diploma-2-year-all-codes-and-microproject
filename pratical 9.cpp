#include <iostream>
using namespace std;

class Account 
{ 
public: 
    int accno; 
    double bal; 
    
    void getdata()  
    { 
        cout << "Enter account number: "; 
        cin >> accno; 
        cout << "Enter balance: "; 
        cin >> bal; 
    } 
    
    void putdata()  
    { 
        if (bal > 10000)  
        { 
            cout << "Account Number: " << accno << endl; 
            cout << "Balance: " << bal << endl; 
        } 
    } 
};

int main()  
{ 
    Account accounts[10]; // Array of objects to store data for 10 accounts 
    
    // Accept data for 10 accounts 
    for (int i = 0; i < 10; i++)  // Changed loop condition
    { 
        cout << "\nEnter details for account " << i + 1 << ":\n"; 
        accounts[i].getdata(); 
    } 
    
    // Display details of accounts having balance greater than 10,000
    cout << "\nAccounts with balance greater than 10,000:\n"; 
    for (int i = 0; i < 10; i++)  
    { 
        accounts[i].putdata(); 
    } 
    
    return 0; 
}
