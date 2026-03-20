import matplotlib.pyplot as plt

def scanline_fill(polygon):
    # Step 1: Find ymin and ymax
    ymin = min(y for x, y in polygon)
    ymax = max(y for x, y in polygon)

    # Step 2: Create Edge Table
    edge_table = []
    n = len(polygon)

    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        # Ignore horizontal edges
        if y1 == y2:
            continue

        # Ensure y1 < y26
        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        edge = {
            "ymin": y1,
            "ymax": y2,
            "x": x1,
            "inv_slope": (x2 - x1) / (y2 - y1)
        }

        edge_table.append(edge)

    # Step 3: Scan line processing
    filled_points = []

    for y in range(ymin, ymax + 1):
        intersections = []

        # Find intersections with edges
        for edge in edge_table:
            if edge["ymin"] <= y < edge["ymax"]:
                x = edge["x"] + (y - edge["ymin"]) * edge["inv_slope"]
                intersections.append(x)

        # Sort intersections
        intersections.sort()

        # Fill between pairs
        for i in range(0, len(intersections), 2):
            if i + 1 < len(intersections):
                x_start = int(round(intersections[i]))
                x_end = int(round(intersections[i + 1]))

                for x in range(x_start, x_end + 1):
                    filled_points.append((x, y))

    return filled_points


# Example polygon (Pentagon)
# polygon = [(2, 2), (8, 3), (10, 7), (6, 10), (3, 7)]
polygon = [
    (5, 2), (7, 0), (9, 2),
    (10, 5), (5, 10),
    (0, 5), (1, 2), (3, 0)
]

filled_pixels = scanline_fill(polygon)

# Plot result
x_vals = [p[0] for p in filled_pixels]
y_vals = [p[1] for p in filled_pixels]

plt.scatter(x_vals, y_vals, s=10)
plt.title("Scan Line Polygon Filling")
plt.gca().invert_yaxis()
plt.show()