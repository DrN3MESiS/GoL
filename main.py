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
import json
import os
import sys
ON = 255
OFF = 0
vals = [ON, OFF]
GRID = np.array([])
GRID_SIZE = 100


# CONFIGURATIONS

def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)


# Still Lifes
def _loadBlock(i, j, grid):
    """adds a Block with top left cell at (i, j)"""
    Block = np.array([[255,    255],
                      [255,  255]])
    grid[i:i+2, j:j+2] = Block


def _loadBeehive(i, j, grid):
    """adds a Beehive with top left cell at (i, j)"""
    Beehive = np.array([[0,    255, 255, 0],
                        [255,  0, 0, 255],
                        [0,  255, 255, 0]])
    grid[i:i+4, j:j+3] = Beehive


def _loadLoaf(i, j, grid):
    """adds a Loaf with top left cell at (i, j)"""
    Loaf = np.array([[0,    255, 255, 0],
                     [255,  0, 0, 255],
                     [0,  255, 0, 255],
                     [0,  0, 255, 0]])
    grid[i:i+4, j:j+4] = Loaf


def _loadBoat(i, j, grid):
    """adds a Boat with top left cell at (i, j)"""
    Boat = np.array([[255,    255, 0],
                     [255,  0, 255],
                     [0,  255, 0]])
    grid[i:i+3, j:j+3] = Boat


def _loadTub(i, j, grid):
    """adds a Tub with top left cell at (i, j)"""
    Tub = np.array([[0,    255, 0],
                    [255,  0, 255],
                    [0,  255, 0]])
    grid[i:i+3, j:j+3] = Tub


# Oscilators

def _loadBlinker(i, j, grid):
    """adds a Blinker with top left cell at (i, j)"""
    Blinker = np.array([[255, 255, 255]])
    grid[i:i+1, j:j+3] = Blinker


def _loadToad(i, j, grid):
    """adds a Toad with top left cell at (i, j)"""
    Toad = np.array([[0,    0, 255, 0],
                     [255,  0, 0, 255],
                     [255,  0, 0, 255],
                     [0,  255, 0, 0]])
    grid[i:i+4, j:j+4] = Toad


def _loadBeacon(i, j, grid):
    """adds a Beacon with top left cell at (i, j)"""
    Beacon = np.array([[255, 255, 0, 0],
                       [255, 255, 0, 0],
                       [0,  0, 255, 255],
                       [0,  0, 255, 255]])
    grid[i:i+4, j:j+4] = Beacon

# Spaceships


def _loadGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 255],
                       [255,  0, 255],
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider


def _loadLightWeightSpaceship(i, j, grid):
    """adds a LightWeightSpaceship with top left cell at (i, j)"""
    LightWeightSpaceship = np.array([[255, 0, 0, 255, 0],
                                     [0, 0, 0, 0, 255],
                                     [255,  0, 0, 0, 255],
                                     [0,  255, 255, 255, 255]])
    grid[i:i+4, j:j+5] = LightWeightSpaceship

# Etc


def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    newGrid = ApplyRules(grid)

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]

    return img,


def ApplyRules(grid: GRID) -> GRID:
    """Applies the rules to to the grid, and returns the modified/updated grid"""
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


def LoadDataFromTXT(filename: str) -> dict:
    configFile = open(filename, "r")
    rows = configFile.readlines()
    configFile.close()

    data = {"mode": "txt"}
    patterns = []

    i = 0
    for line in rows:
        if len(line) == 0:
            i += 1
            continue
        if i == 0:
            n = line.split(" ")
            if len(n) < 1:
                break
            data["universe_size"] = int(n[0])
            i += 1
            continue
        else:
            coord = line.split(" ")
            (x, y) = coord

            patterns.append(
                {
                    "x": int(x.rstrip().strip()),
                    "y": int(y.rstrip().strip())
                }
            )
        i += 1

    if len(patterns) > 0:
        data["patterns"] = patterns

    return data


def LoadDataFromJSON(filename: str) -> dict:
    configFile = open(filename, "r")

    data = json.loads(configFile.read())
    configFile.close()
    data["mode"] = "json"

    return data


def ApplyConfiguration(config: dict, grid: GRID) -> GRID:
    GRID_SIZE = config.get("universe_size")
    if GRID_SIZE == None:
        print("\t[CONFIG_KEY_NOT_FOUND] Universe Size value was set to default (100)")
        GRID_SIZE = 100
    grid = np.zeros(GRID_SIZE*GRID_SIZE).reshape(GRID_SIZE, GRID_SIZE)

    patterns = config.get("patterns")
    if patterns == None:
        print("\t[CONFIG_KEY_NOT_FOUND] Patterns value was not found")
        sys.exit()
        return grid

    mode = config.get("mode")
    if mode == "txt":
        for pat in patterns:
            x = pat.get("x")
            y = pat.get("y")

            if x > GRID_SIZE or x < 0:
                print("\t[PATTERN_COORDS_INVALID] Skipping invalid pattern")
                continue
            if y > GRID_SIZE or y < 0:
                print("\t[PATTERN_COORDS_INVALID] Skipping invalid pattern")
                continue

            grid[x][y] = 255
    elif mode == "json":
        for pat in patterns:
            patType = pat.get("type")
            if patType == None:
                print("\t[PATTERN_TYPE_NOT_FOUND] Skipping incomplete pattern")
                continue
            patCoords = pat.get("topLeftCornerPosition")
            if patType == None:
                print(
                    "[TOP_LEFT_CORNER_POSITION_NOT_FOUND] Skipping incomplete pattern")
                continue

            patCordX = patCoords.get("x")
            patCordY = patCoords.get("y")
            if patCordX == None or patCordY == None:
                print("[COORDINATES_NOT_FOUND] Skipping incomplete pattern")
                continue

            if patCordX > (GRID_SIZE-1) or patCordX < 0 or patCordY > (GRID_SIZE-1) or patCordY < 0:
                print(
                    "[INVALID_COORDINATES] Skipping invalid pattern")
                continue

            # Still Lifes
            if patType == "block":
                _loadBlock(patCordX, patCordY, grid)
                continue
            elif patType == "beehive":
                _loadBeehive(patCordX, patCordY, grid)
                continue
            elif patType == "loaf":
                _loadLoaf(patCordX, patCordY, grid)
                continue
            elif patType == "boat":
                _loadBoat(patCordX, patCordY, grid)
                continue
            elif patType == "tub":
                _loadTub(patCordX, patCordY, grid)
                continue

            # Oscilators
            if patType == "blinker":
                _loadBlinker(patCordX, patCordY, grid)
                continue
            elif patType == "toad":
                _loadToad(patCordX, patCordY, grid)
                continue
            elif patType == "beacon":
                _loadBeacon(patCordX, patCordY, grid)
                continue

            # Spaceships
            if patType == "glider":
                _loadGlider(patCordX, patCordY, grid)
                continue
            elif patType == "light-weight spaceship":
                _loadLightWeightSpaceship(patCordX, patCordY, grid)
                continue

    return grid


def main():
    grid = np.array([])

    parser = argparse.ArgumentParser(
        description="Runs DrN3MESiS (Alan Maldonado) Implementation of Conway's Game of Life.")
    parser.add_argument(
        "configFilename", help="Filename of the Configuration File")

    args = parser.parse_args()

    if not os.path.isfile(args.configFilename):
        print("[NOT_FOUND] File was not found or is not accessible")
        sys.exit()
    print("[LOADED] Primary Setup Complete")

    simConfig = dict()
    if str(args.configFilename).endswith(".json"):
        simConfig = LoadDataFromJSON(args.configFilename)
    elif str(args.configFilename).endswith(".txt"):
        simConfig = LoadDataFromTXT(args.configFilename)

    print("[LOADED] Secondary Setup Complete")
    grid = ApplyConfiguration(simConfig, grid)
    print("[LOADED] Third Setup Complete; Applied Configuration")
    print("[SUCCESS] Started Conway's Game of Life Simulation")

    updateInterval = 1000
    timeSpeed = 0.05

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update,
                                  fargs=(img, grid, GRID_SIZE, ),
                                  frames=200,
                                  interval=updateInterval * timeSpeed,
                                  save_count=50,
                                  repeat=False)

    plt.show()


# call main
if __name__ == '__main__':
    main()
