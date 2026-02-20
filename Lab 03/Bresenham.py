import matplotlib.pyplot as plt

def bresenham_m_less_than_1(x1, y1, x2, y2):
    points = []

    dx = x2 - x1
    dy = y2 - y1

    p = 2 * dy - dx
    x = x1
    y = y1

    points.append((x, y))

    while x < x2:
        x += 1
        if p < 0:
            p = p + 2 * dy
        else:
            y += 1
            p = p + 2 * dy - 2 * dx

        points.append((x, y))

    return points


# Example
x1, y1 = 2, 2
x2, y2 = 10, 6

points = bresenham_m_less_than_1(x1, y1, x2, y2)

# Plotting
x_vals = [p[0] for p in points]
y_vals = [p[1] for p in points]

plt.scatter(x_vals, y_vals)
plt.plot(x_vals, y_vals)
plt.title("Bresenham Line (m < 1)")
plt.grid()
plt.show()
