#include<iostream>
#include<string>

using namespace std;

// Define the Student structure
struct Student {
    int id;
    string name;
    int roll_no;
    string class_name; // Changed 'class' to 'class_name' because 'class' is a reserved keyword in C++
};

// Function to input student data
void inputStudentData(Student &s) {
    cout << "Enter student ID: ";
    cin >> s.id;
    cin.ignore(); // To ignore the newline character left in the buffer
    
    cout << "Enter student name: ";
    getline(cin, s.name);
    
    cout << "Enter roll number: ";
    cin >> s.roll_no;
    cin.ignore(); // To ignore the newline character left in the buffer
    
    cout << "Enter class name: ";
    getline(cin, s.class_name);
}

// Function to display student data
void displayStudentData(const Student &s) {
    cout << "\nStudent Information:" << endl;
    cout << "ID: " << s.id << endl;
    cout << "Name: " << s.name << endl;
    cout << "Roll Number: " << s.roll_no << endl;
    cout << "Class: " << s.class_name << endl;
}

int main() {
    Student student;

    // Input student data
    inputStudentData(student);
    
    // Display student data
    displayStudentData(student);

    return 0;
}
