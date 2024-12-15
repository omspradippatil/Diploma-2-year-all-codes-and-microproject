#include <graphics.h>
#include <iostream>
#include <conio.h>
#include <windows.h> // For Sleep()
#include <cstdlib>   // For rand()

using namespace std;

void enemycar(int x, int y) {
    setcolor(WHITE);
    rectangle(x + 1, y, x + 49, y + 100);
    rectangle(x + 1, y + 25, x + 49, y + 75);
    setfillstyle(SOLID_FILL, YELLOW);
    floodfill((x + x + 50) / 2, (y + y + 100) / 2, WHITE);
}

void mycar(int x, int y) {
    setcolor(WHITE);
    rectangle(x + 1, y, x + 49, y + 100);
    rectangle(x + 1, y + 25, x + 49, y + 75);
    setfillstyle(SOLID_FILL, RED);
    floodfill((x + x + 50) / 2, (y + y + 100) / 2, WHITE);
}

void clearcar(int x, int y) {
    setcolor(BLACK);
    rectangle(x + 1, y, x + 49, y + 100);
    rectangle(x + 1, y + 25, x + 49, y + 75);
    setfillstyle(SOLID_FILL, BLACK);
    floodfill((x + x + 50) / 2, (y + y + 100) / 2, BLACK);
}

int main() {
    // Initialize graphics
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Game variables
    int x = 300, y = 350, ch, life = 3, score = 0;
    int level = 1;

    cout << "Welcome to Thunder Racer!" << endl;
    cout << "Save the princess by avoiding enemy cars." << endl;
    cout << "Press <Esc> to exit the game.\n" << endl;

    while (life > 0 && level <= 5) {
        int accident = 0;
        int y1 = 1, x1 = 250 + ((rand() % 3) * 50);
        int y2 = 1, x2 = 250 + ((rand() % 3) * 50);
        score += 10;

        while (y1 < getmaxy() - 1) {
            clearcar(x1, y1);
            clearcar(x2, y2);
            y1 += 1;
            y2 += 1;

            if (accident) break;

            enemycar(x1, y1);
            enemycar(x2, y2);
            mycar(x, y);

            Sleep(10 - level); // Delay based on level

            // Handle user input
            if (kbhit()) {
                ch = getch();
                switch (ch) {
                    case 27: // ESC key to exit
                        closegraph();
                        return 0;

                    case 75: // Left arrow key
                        clearcar(x, y);
                        if (x > 250) x -= 50;
                        mycar(x, y);
                        break;

                    case 77: // Right arrow key
                        clearcar(x, y);
                        if (x < 350) x += 50;
                        mycar(x, y);
                        break;

                    case 72: // Up arrow key
                        clearcar(x, y);
                        if (y > 0) y -= 5;
                        mycar(x, y);
                        break;

                    case 80: // Down arrow key
                        clearcar(x, y);
                        if (y < getmaxy() - 105) y += 5;
                        mycar(x, y);
                        break;
                }
            }

            // Check for collision
            if ((x == x1 || x == x2) &&
                (((y - y1) < 100 && (y - y1) > 0) || ((y - y2) < 100 && (y - y2) > 0))) {
                accident = 1;
                life--;
                score -= 10;
                break;
            }
        }

        if (accident) {
            if (life == 0) {
                setcolor(RED);
                outtextxy(200, 200, "GAME OVER");
                outtextxy(200, 220, "You could not save her!");
                break;
            } else {
                outtextxy(200, 200, "You lost a life!");
                Sleep(1000);
                cleardevice(); // Clear the screen for the next round
            }
        }

        level++;
    }

    // End of game
    if (life > 0) {
        setcolor(GREEN);
        outtextxy(200, 200, "Congratulations! You saved her!");
    }

    getch();
    closegraph();
    return 0;
}
