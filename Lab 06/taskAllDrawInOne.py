import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# Helper Functions
# ------------------------------

def print_points(label, points):
    print(f"\n{label}:")
    for i, (x, y) in enumerate(points):
        print(f"P{i+1}: ({x:.2f}, {y:.2f})")


def plot_polygon(points, title, color):
    pts = np.array(points + [points[0]])
    plt.plot(pts[:, 0], pts[:, 1], marker='o', color=color, label=title)


def translate(points, tx, ty):
    return [(x + tx, y + ty) for x, y in points]


def scale(points, sx, sy):
    return [(x * sx, y * sy) for x, y in points]


def rotate(points, angle_deg):
    angle = np.radians(angle_deg)
    cos_a, sin_a = np.cos(angle), np.sin(angle)
    return [(x * cos_a - y * sin_a, x * sin_a + y * cos_a) for x, y in points]


def rotate_about_point(points, angle_deg, cx, cy):
    temp = translate(points, -cx, -cy)
    temp = rotate(temp, angle_deg)
    return translate(temp, cx, cy)


def scale_about_point(points, sx, sy, cx, cy):
    temp = translate(points, -cx, -cy)
    temp = scale(temp, sx, sy)
    return translate(temp, cx, cy)


def composite_transform(points, sx, sy, angle_deg, tx, ty):
    temp = scale(points, sx, sy)
    temp = rotate(temp, angle_deg)
    return translate(temp, tx, ty)


# ------------------------------
# Input Polygon
# ------------------------------

polygon = [[2, 2],
    [5, 1],
    [8, 3],
    [7, 6],
    [4, 8],
    [1, 5]]

print_points("Original Polygon", polygon)

# ------------------------------
# Transformations
# ------------------------------

translated = translate(polygon, 2, 1)
print_points("Translated (tx=2, ty=1)", translated)

scaled = scale(polygon, 2, 1.5)
print_points("Scaled (sx=2, sy=1.5)", scaled)

rotated = rotate(polygon, 45)
print_points("Rotated (45° about origin)", rotated)

rotated_arbitrary = rotate_about_point(polygon, 45, 2, 2)
print_points("Rotated (45° about point (2,2))", rotated_arbitrary)

scaled_arbitrary = scale_about_point(polygon, 1.5, 2, 2, 2)
print_points("Scaled (about point (2,2), sx=1.5, sy=2)", scaled_arbitrary)

composite = composite_transform(polygon, 1.5, 1.5, 30, 2, 2)
print_points("Composite (Scale→Rotate→Translate)", composite)

# ------------------------------
# Plotting
# ------------------------------

plt.figure(figsize=(8, 8))

plot_polygon(polygon, "Original", 'black')
plot_polygon(translated, "Translated", 'blue')
plot_polygon(scaled, "Scaled", 'green')
plot_polygon(rotated, "Rotated", 'red')
plot_polygon(rotated_arbitrary, "Rotated (Arbitrary)", 'purple')
plot_polygon(scaled_arbitrary, "Scaled (Arbitrary)", 'orange')
plot_polygon(composite, "Composite", 'brown')

plt.legend()
plt.grid()
plt.axis('equal')
plt.title("2D Geometric Transformations")
plt.show()