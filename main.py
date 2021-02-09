"""
conway.py
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import copy

ON = 255
OFF = 0
vals = [ON, OFF]
GRID = np.array([])
GRID_SIZE = 100


def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)


def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 255],
                       [255,  0, 255],
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider


def update(frameNum, img, grid, N):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newGrid = grid.copy()
    # TODO: Implement the rules of Conway's Game of Life
    newGrid = ApplyRules(grid)

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]

    print("> Update")
    return img,

# main() function


def ApplyRules(grid: GRID) -> GRID:
    updatedGrid = np.zeros(GRID_SIZE*GRID_SIZE).reshape(GRID_SIZE, GRID_SIZE)
    tempGrid = grid.copy()

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            curItem = tempGrid[i][j]

            # DEAD
            if curItem == 0:
                neiAm = 0
                # Calculate Neighbours

                # Down
                if i != 0:
                    if tempGrid[i-1][j] >= 255:
                        neiAm += 1

                # Up
                if i != (GRID_SIZE-1):
                    if tempGrid[i+1][j] >= 255:
                        neiAm += 1

                # Left
                if j != 0:
                    if tempGrid[i][j-1] >= 255:
                        neiAm += 1

                # Right
                if j != (GRID_SIZE-1):
                    if tempGrid[i][j+1] >= 255:
                        neiAm += 1

                # Down Left
                if i != 0 and j != 0:
                    if tempGrid[i-1][j-1] >= 255:
                        neiAm += 1

                # Down Right
                if i != 0 and j != (GRID_SIZE-1):
                    if tempGrid[i-1][j+1] >= 255:
                        neiAm += 1

                # Up Right
                if i != (GRID_SIZE-1) and j != (GRID_SIZE-1):
                    if tempGrid[i+1][j+1] >= 255:
                        neiAm += 1

                # Up Left
                if i != (GRID_SIZE-1) and j != 0:
                    if tempGrid[i+1][j-1] >= 255:
                        neiAm += 1

                if neiAm == 3:
                    updatedGrid[i][j] = 255
                    continue

            # ALIVE
            if curItem >= 255:
                neiAm = 0

                # Calculate Neighbours
                if i != 0:
                    if tempGrid[i-1][j] >= 255:
                        neiAm += 1

                if i != (GRID_SIZE-1):
                    if tempGrid[i+1][j] >= 255:
                        neiAm += 1

                if j != 0:
                    if tempGrid[i][j-1] >= 255:
                        neiAm += 1

                if j != (GRID_SIZE-1):
                    if tempGrid[i][j+1] >= 255:
                        neiAm += 1

                if i != 0 and j != 0:
                    if tempGrid[i-1][j-1] >= 255:
                        neiAm += 1

                if i != 0 and j != (GRID_SIZE-1):
                    if tempGrid[i-1][j+1] >= 255:
                        neiAm += 1

                if i != (GRID_SIZE-1) and j != (GRID_SIZE-1):
                    if tempGrid[i+1][j+1] >= 255:
                        neiAm += 1

                if i != (GRID_SIZE-1) and j != 0:
                    if tempGrid[i+1][j-1] >= 255:
                        neiAm += 1

                # RULES

                # Rule 1
                if neiAm < 2:
                    updatedGrid[i][j] = 0
                    continue
                # Rule 2
                if neiAm == 2 or neiAm == 3:
                    updatedGrid[i][j] = 255
                    continue
                # Rule 3
                if neiAm > 3:
                    updatedGrid[i][j] = 0
                    continue

    return updatedGrid


def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(
        description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments

    # set animation update interval
    updateInterval = 50

    # declare grid
    grid = np.array([])
    # populate grid with random on/off - more off than on
    # grid = randomGrid(N)
    # Uncomment lines to see the "glider" demo
    grid = np.zeros(GRID_SIZE*GRID_SIZE).reshape(GRID_SIZE, GRID_SIZE)
    addGlider(1, 1, grid)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, GRID_SIZE, ),
                                  frames=10,
                                  interval=updateInterval,
                                  save_count=50)

    plt.show()


# call main
if __name__ == '__main__':
    main()
