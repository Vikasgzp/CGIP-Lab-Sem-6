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

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    # to be 100% accurate use p=1.25-r
    # i have used this to just speedup calculation
    points = []
    plot_circle_points(xc, yc, x, y, points)

    while x < y:
        x += 1

        if p < 0:
            p = p + 2*x + 1
        else:
            y -= 1
            p = p + 2*x - 2*y + 1

        plot_circle_points(xc, yc, x, y, points)

    return points


# Example
xc, yc = 0, 0
radius = 10

points = midpoint_circle(xc, yc, radius)

x_vals = [p[0] for p in points]
y_vals = [p[1] for p in points]

plt.scatter(x_vals, y_vals)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Midpoint Circle Drawing Algorithm")
plt.grid(True)
plt.show()