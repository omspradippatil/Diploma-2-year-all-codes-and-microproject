#include<iostream>
using namespace std;

int main() {
    int number, i;
    bool isPrime = true;  // Assume the number is prime initially

    cout << "Enter a number: ";
    cin >> number;

    // Step 1: Check if the number is less than or equal to 1
    if (number <= 1) {
        isPrime = false;  // Numbers <= 1 are not prime
    }

    // Step 2: Loop through numbers from 2 to number-1
    for (i = 2; i < number; i++) {
        // Step 3: Check if the number is divisible by i
        if (number % i == 0) {
            isPrime = false;  // If divisible, it's not prime
            break;  // Exit the loop early since we found a divisor
        }
    }

    // Step 4: Output the result
    if (isPrime)
        cout << number << " is a prime number." << endl;
    else
        cout << number << " is not a prime number." << endl;

    return 0;
}
