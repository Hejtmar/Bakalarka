from matplotlib import pyplot as plt
xValues = [220, 230, 240, 250]
yValues = [38.77, 43.73, 46.23, 43.46]

plt.figure(0)
plt.ylim(30,50)
plt.plot(xValues, yValues, "*r")
plt.xlabel("Print temperature [deg]")
plt.ylabel("Tensile strength [MPa]")
plt.grid()
plt.title("Print temperature vs. strentgh")
plt.show()
plt.subplot
