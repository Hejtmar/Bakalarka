from matplotlib import pyplot as plt
xValues = [100, 80, 60, 40, 20]
yValues = [46.23, 46.30, 45.14, 37.03, 39.38]

plt.figure(0)
plt.plot(xValues, yValues, "*r")
plt.xlabel("Infill percentage [%]")
plt.ylabel("Tensile strength [MPa]")
plt.grid()
plt.title("Infill percentage vs. strentgh")
plt.show()
plt.subplot
