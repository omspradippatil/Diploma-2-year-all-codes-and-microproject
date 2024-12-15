#include <iostream>
#include <cstdlib>
#include <ctime>

void playGame() {
    std::srand(std::time(0)); // Seed the random number generator
    int numberToGuess = std::rand() % 100 + 1; // Random number between 1 and 100
    int guess;
    int attempts = 0;

    std::cout << "Welcome to the Number Guessing Game!" << std::endl;
    std::cout << "I have selected a number between 1 and 100. Try to guess it!" << std::endl;

    do {
        std::cout << "Enter your guess: ";
        std::cin >> guess;
        attempts++;

        if (guess > numberToGuess) {
            std::cout << "Too high! Try again." << std::endl;
        } else if (guess < numberToGuess) {
            std::cout << "Too low! Try again." << std::endl;
        } else {
            std::cout << "Congratulations! You guessed the number in " << attempts << " attempts." << std::endl;
        }
    } while (guess != numberToGuess);
}

int main() {
    char playAgain;

    do {
        playGame();
        std::cout << "Do you want to play again? (y/n): ";
        std::cin >> playAgain;
    } while (playAgain == 'y' || playAgain == 'Y');

    std::cout << "Thank you for playing!" << std::endl;
    return 0;
}