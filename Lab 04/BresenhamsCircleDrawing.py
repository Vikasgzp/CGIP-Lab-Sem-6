import matplotlib.pyplot as plt

def plot_circle_points(xc, yc, x, y, points):
    # 8-way symmetry
    points.extend([
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x)
    ])

def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2*r

    points = []
    plot_circle_points(xc, yc, x, y, points)

    while x <= y:
        x += 1

        if d < 0:
            d = d + 4*x + 6
        else:
            y -= 1
            d = d + 4*(x - y) + 10

        plot_circle_points(xc, yc, x, y, points)

    return points


# Example
xc, yc = 0, 0
radius = 10

points = bresenham_circle(xc, yc, radius)

x_vals = [p[0] for p in points]
y_vals = [p[1] for p in points]

plt.scatter(x_vals, y_vals)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Bresenham Circle Drawing Algorithm")
plt.grid(True)
plt.show()