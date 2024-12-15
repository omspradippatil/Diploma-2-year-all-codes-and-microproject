#include <iostream>
#include <vector>

using namespace std;

const int BOARD_SIZE = 8;

void initializeBoard(vector<vector<char>>& board) {
    // Initialize empty board
    for (int i = 0; i < BOARD_SIZE; ++i) {
        vector<char> row(BOARD_SIZE, '.');
        board.push_back(row);
    }

    // Place white pawns
    for (int i = 0; i < BOARD_SIZE; ++i) {
        board[1][i] = 'P';
    }

    // Place black pawns
    for (int i = 0; i < BOARD_SIZE; ++i) {
        board[6][i] = 'p';
    }
}

void printBoard(const vector<vector<char>>& board) {
    for (const auto& row : board) {
        for (const auto& cell : row) {
            cout << cell << ' ';
        }
        cout << endl;
    }
}

int main() {
    vector<vector<char>> board;
    initializeBoard(board);
    printBoard(board);
    return 0;
}