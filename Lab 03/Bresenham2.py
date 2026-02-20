import matplotlib.pyplot as plt

def bresenham_all_cases(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dx > dy:
        p = 2 * dy - dx
        while x1 != x2:
            points.append((x1, y1))
            x1 += sx
            if p < 0:
                p += 2 * dy
            else:
                y1 += sy
                p += 2 * dy - 2 * dx
    else:
        p = 2 * dx - dy
        while y1 != y2:
            points.append((x1, y1))
            y1 += sy
            if p < 0:
                p += 2 * dx
            else:
                x1 += sx
                p += 2 * dx - 2 * dy

    points.append((x2, y2))
    return points


# Example
x1, y1 = 2, 2
x2, y2 = 12, 6   # try different slopes

points = bresenham_all_cases(x1, y1, x2, y2)

x_vals = [p[0] for p in points]
y_vals = [p[1] for p in points]

plt.scatter(x_vals, y_vals)
plt.plot(x_vals, y_vals)
plt.title("Bresenham Line (All Slopes)")
plt.grid()
plt.show()
