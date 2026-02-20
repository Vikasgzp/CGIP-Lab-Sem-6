import matplotlib.pyplot as plt

def dda_without_slope(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1

    x_points = []
    y_points = []

    for _ in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc

    return x_points, y_points


# Example usage
x, y = dda_without_slope(2, 2, 10, 6)
plt.plot(x, y, marker='o')
plt.title("DDA Line (Without Slope Cases)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
