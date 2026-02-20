import matplotlib.pyplot as plt

def dda_with_slope(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    x_points = []
    y_points = []

    # Vertical line
    if dx == 0:
        y_step = 1 if y2 > y1 else -1
        for y in range(y1, y2 + y_step, y_step):
            x_points.append(x1)
            y_points.append(y)

    # Horizontal line
    elif dy == 0:
        x_step = 1 if x2 > x1 else -1
        for x in range(x1, x2 + x_step, x_step):
            x_points.append(x)
            y_points.append(y1)

    else:
        m = dy / dx

        # Gentle slope (|m| ≤ 1)
        if abs(m) <= 1:
            x_step = 1 if x2 > x1 else -1
            y = y1
            for x in range(x1, x2 + x_step, x_step):
                x_points.append(x)
                y_points.append(round(y))
                y += m * x_step

        # Steep slope (|m| > 1)
        else:
            y_step = 1 if y2 > y1 else -1
            x = x1
            for y in range(y1, y2 + y_step, y_step):
                x_points.append(round(x))
                y_points.append(y)
                x += (1 / m) * y_step

    return x_points, y_points


# Example usage
x, y = dda_with_slope(2, 2, 6, 10)
plt.plot(x, y, marker='o')
plt.title("DDA Line (With Slope Cases)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
