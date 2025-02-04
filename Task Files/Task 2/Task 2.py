import matplotlib.pyplot as plt
import numpy as np
import math
import os.path
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath("__file__")))))
import PlanetData as Pd

fig = plt.figure()
ax = fig.add_subplot()
ax.set_aspect('equal', adjustable='box')

planet_system = Pd.Ursae_Majoris_47

for i in range(len(planet_system)):
    x_coords = []
    y_coords = []

    # Loop through values of theta
    for theta in np.arange(0, (2*math.pi)+1, 0.1):
        semi_major = float(planet_system[i][1])
        eccen = float(planet_system[i][2])
        # Calculate radius
        radius = (semi_major*(1-(eccen*eccen)))/(1-eccen*math.cos(theta))
        # Calculate coordinates
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        x_coords.append(x)
        y_coords.append(y)
        # Plot graph
    plt.plot(x_coords, y_coords, label=planet_system[i][7])

plt.plot(0, 0, marker="o", markersize=20, markerfacecolor="yellow")
plt.title("Ursae Majoris 47 system")
plt.xlabel("X (AU)")
plt.ylabel("Y (AU)")
plt.legend(loc="upper right")

plt.show()
