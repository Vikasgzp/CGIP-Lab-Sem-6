#include <iostream>
using namespace std;

// Clipping window
const double xmin = 2, ymin = 2, xmax = 6, ymax = 6;

// Region codes for Cohen–Sutherland
const int INSIDE = 0; // 0000
const int LEFT = 1;   // 0001
const int RIGHT = 2;  // 0010
const int BOTTOM = 4; // 0100
const int TOP = 8;    // 1000

// Compute region code
int computeCode(double x, double y) {
    int code = INSIDE;

    if (x < xmin) code |= LEFT;
    else if (x > xmax) code |= RIGHT;

    if (y < ymin) code |= BOTTOM;
    else if (y > ymax) code |= TOP;

    return code;
}

// Cohen–Sutherland Algorithm
void cohenSutherland(double x1, double y1, double x2, double y2) {
    int code1 = computeCode(x1, y1);
    int code2 = computeCode(x2, y2);

    bool accept = false;

    while (true) {
        if ((code1 == 0) && (code2 == 0)) {
            accept = true;
            break;
        }
        else if (code1 & code2) {
            break;
        }
        else {
            double x, y;
            int code_out = code1 ? code1 : code2;

            if (code_out & TOP) {
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1);
                y = ymax;
            }
            else if (code_out & BOTTOM) {
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1);
                y = ymin;
            }
            else if (code_out & RIGHT) {
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1);
                x = xmax;
            }
            else {
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1);
                x = xmin;
            }

            if (code_out == code1) {
                x1 = x; y1 = y;
                code1 = computeCode(x1, y1);
            } else {
                x2 = x; y2 = y;
                code2 = computeCode(x2, y2);
            }
        }
    }

    if (accept)
        cout << "Accepted: (" << x1 << ", " << y1 << ") to (" << x2 << ", " << y2 << ")\n";
    else
        cout << "Rejected\n";
}

// Liang–Barsky Algorithm
void liangBarsky(double x1, double y1, double x2, double y2) {
    double dx = x2 - x1;
    double dy = y2 - y1;

    double p[4] = {-dx, dx, -dy, dy};
    double q[4] = {x1 - xmin, xmax - x1, y1 - ymin, ymax - y1};

    double t1 = 0.0, t2 = 1.0;

    for (int i = 0; i < 4; i++) {
        if (p[i] == 0) {
            if (q[i] < 0) {
                cout << "Rejected\n";
                return;
            }
        } else {
            double t = q[i] / p[i];
            if (p[i] < 0)
                t1 = max(t1, t);
            else
                t2 = min(t2, t);
        }
    }

    if (t1 > t2) {
        cout << "Rejected\n";
        return;
    }

    double nx1 = x1 + t1 * dx;
    double ny1 = y1 + t1 * dy;
    double nx2 = x1 + t2 * dx;
    double ny2 = y1 + t2 * dy;

    cout << "Accepted: (" << nx1 << ", " << ny1 << ") to (" << nx2 << ", " << ny2 << ")\n";
}

// Test function
void testLine(double x1, double y1, double x2, double y2) {
    cout << "\nLine: (" << x1 << ", " << y1 << ") to (" << x2 << ", " << y2 << ")\n";

    cout << "Cohen-Sutherland: ";
    cohenSutherland(x1, y1, x2, y2);

    cout << "Liang-Barsky:     ";
    liangBarsky(x1, y1, x2, y2);
}

int main() {
    testLine(3, 5, 3, 9);
    testLine(1, 8, 1, 10);
    testLine(1, 2, 7, 7);

    return 0;
}