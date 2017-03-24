# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:43:12 2016

@author: Smoothie
"""

import numpy as np
iterations = 1000
totalTime = 30#s
dt = totalTime / iterations

rodLength = 2500#mm
steps = 100#
dx = rodLength / steps#mm

alpha = 0.5
constant = alpha * dt / (dx**2)

initialTemperature = 25
boundaryTemperature = 100

grid = np.full(steps, initialTemperature)
grid[0] = boundaryTemperature
previousGrid = grid
data = []

for i in range(iterations):
    for j in range(steps):
        if (j!=0):
            try:
                previousGrid[j] += constant*previousGrid[j+1]  +  (1-2*constant)*previousGrid[j]  +  constant*previousGrid[j-1]
            except Exception:
                endDerivative = previousGrid[steps-1] - previousGrid[steps-2]
                endPoint = previousGrid[steps-1] + endDerivative
                previousGrid[j] += constant*endPoint  +  (1-2*constant)*previousGrid[j]  +  constant*previousGrid[j-1]
    data.append(previousGrid.tolist())
                