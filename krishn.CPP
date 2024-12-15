#include <graphics.h>
#include <conio.h>

void drawKrishnaFace(int x, int y) {
    setcolor(BLUE);
    setfillstyle(SOLID_FILL, BLUE);
    circle(x, y, 30);  // Face
    floodfill(x, y, BLUE);

    // Eyes
    setcolor(WHITE);
    setfillstyle(SOLID_FILL, WHITE);
    ellipse(x - 10, y - 10, 0, 360, 5, 10);
    ellipse(x + 10, y - 10, 0, 360, 5, 10);
    floodfill(x - 10, y - 10, WHITE);
    floodfill(x + 10, y - 10, WHITE);

    // Pupils
    setcolor(BLACK);
    setfillstyle(SOLID_FILL, BLACK);
    circle(x - 10, y - 10, 2);
    circle(x + 10, y - 10, 2);
    floodfill(x - 10, y - 10, BLACK);
    floodfill(x + 10, y - 10, BLACK);

    // Mouth
    setcolor(RED);
    arc(x, y + 10, 190, 350, 10);
}

void drawFlute(int x, int y) {
    setcolor(YELLOW);
    setfillstyle(SOLID_FILL, YELLOW);
    rectangle(x - 40, y + 20, x + 40, y + 25);  // Flute
    floodfill(x, y + 22, YELLOW);

    // Flute holes
    setcolor(BLACK);
    for (int i = -30; i <= 30; i += 15) {
        circle(x + i, y + 22, 2);
        floodfill(x + i, y + 22, BLACK);
    }
}

void drawPeacockFeather(int x, int y) {
    // Drawing a simple peacock feather with two colors
    setcolor(GREEN);
    setfillstyle(SOLID_FILL, GREEN);
    ellipse(x - 5, y - 40, 0, 360, 5, 15);  // Feather base
    floodfill(x - 5, y - 40, GREEN);

    setcolor(BLUE);
    setfillstyle(SOLID_FILL, BLUE);
    ellipse(x - 5, y - 55, 0, 360, 7, 20);  // Feather top
    floodfill(x - 5, y - 55, BLUE);
}

void drawKrishna() {
    int x = 320, y = 240;

    // Draw face and features
    drawKrishnaFace(x, y);

    // Draw flute
    drawFlute(x, y);

    // Draw peacock feather
    drawPeacockFeather(x, y - 30);
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "C:\\Turboc3\\BGI");

    drawKrishna();

    getch();
    closegraph();
    return 0;
}
