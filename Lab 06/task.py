import numpy as np
import matplotlib.pyplot as plt
import math

# Original polygon (given in PDF)
polygon = np.array([
    [2, 2],
    [5, 1],
    [8, 3],
    [7, 6],
    [4, 8],
    [1, 5]
])

# Close polygon for plotting
def close_polygon(poly):
    return np.vstack([poly, poly[0]])

# Plot function
def plot_polygons(original, transformed, title):
    plt.figure()
    plt.plot(*close_polygon(original).T, 'bo-', label='Original')
    plt.plot(*close_polygon(transformed).T, 'ro-', label='Transformed')
    
    # Label points
    for i, (x, y) in enumerate(original):
        plt.text(x, y, f'O{i}', color='blue')
    for i, (x, y) in enumerate(transformed):
        plt.text(x, y, f'T{i}', color='red')

    plt.title(title)
    plt.legend()
    plt.grid()
    plt.axis('equal')
    plt.show()

# -----------------------------
# Task 1: Translation
# -----------------------------
def translate(poly, tx, ty):
    return poly + np.array([tx, ty])

translated = translate(polygon, 3, 2)
plot_polygons(polygon, translated, "Task 1: Translation")

# -----------------------------
# Task 2: Scaling about Origin
# -----------------------------
def scale(poly, sx, sy):
    return poly * np.array([sx, sy])

scaled = scale(polygon, 2, 1.5)
plot_polygons(polygon, scaled, "Task 2: Scaling about Origin")

# -----------------------------
# Task 3: Rotation about Origin
# -----------------------------
def rotate(poly, theta):
    rad = math.radians(theta)
    rotation_matrix = np.array([
        [math.cos(rad), -math.sin(rad)],
        [math.sin(rad),  math.cos(rad)]
    ])
    return poly @ rotation_matrix.T

rotated = rotate(polygon, 45)
plot_polygons(polygon, rotated, "Task 3: Rotation about Origin")

# -----------------------------
# Task 4: Rotation about Arbitrary Point (4,4)
# -----------------------------
def rotate_about_point(poly, theta, px, py):
    translated = poly - np.array([px, py])
    rotated = rotate(translated, theta)
    return rotated + np.array([px, py])

rotated_arbitrary = rotate_about_point(polygon, 45, 4, 4)
plot_polygons(polygon, rotated_arbitrary, "Task 4: Rotation about Arbitrary Point")

# -----------------------------
# Task 5: Scaling about Arbitrary Point (4,4)
# -----------------------------
def scale_about_point(poly, sx, sy, px, py):
    translated = poly - np.array([px, py])
    scaled = scale(translated, sx, sy)
    return scaled + np.array([px, py])

scaled_arbitrary = scale_about_point(polygon, 2, 1.5, 4, 4)
plot_polygons(polygon, scaled_arbitrary, "Task 5: Scaling about Arbitrary Point")

# -----------------------------
# Task 6: Composite Transformation
# (Scaling → Rotation → Translation)
# -----------------------------
def composite(poly):
    poly1 = scale(poly, 2, 1.5)
    poly2 = rotate(poly1, 45)
    poly3 = translate(poly2, 3, 2)
    return poly3

composite_result = composite(polygon)
plot_polygons(polygon, composite_result, "Task 6: Composite Transformation")