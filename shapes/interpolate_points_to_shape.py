# import shapely.affinity
# from shapely.geometry import Point
# import matplotlib.pyplot as plt

# circle = Point(100, 100).buffer(1)
# new_circle = shapely.affinity.scale(circle, 20, 20)

# print(new_circle)

# xs, ys = new_circle.exterior.xy
# fig, axs = plt.subplots()
# axs.fill(xs, ys, alpha=0.5, fc='r', ec='none')
# axs.set_aspect('equal', adjustable='box')
# axs.grid()

# plt.show()

import numpy as np
import matplotlib.pyplot as plt

def circle_points(r, n, x_c=0.0, y_c=0.0):
    circles = []
    bearings = []
    for r, n in zip(r, n):
        t = np.linspace(0, 2*np.pi, n, endpoint=False)
        x = r * np.cos(t) + x_c
        y = r * np.sin(t) + y_c
        circles.append(np.c_[x, y])
        bearings.append(np.c_[(t + np.pi)])
    return circles, bearings
r = [20, 40, 80, 100]
n = [5, 7, 9, 13]

circles, bearings = circle_points(r, n, x_c=100, y_c=100)

print(circles)
print(bearings)

fig, ax = plt.subplots()
for circle in circles:
    ax.scatter(circle[:, 0], circle[:, 1])
ax.set_aspect('equal')
plt.show()

x_vals = np.linspace(-12, 12, num=500, endpoint=True)
y_vals = np.linspace(-12, 12, num=500, endpoint=True)
z_vals = np.zeros(len(x_vals))
print(type(x_vals))
print(type(y_vals))
print(type(z_vals))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x_vals, y_vals, z_vals)
ax.set_label('X')
ax.set_label('Y')
ax.set_label('Z')
plt.show()
