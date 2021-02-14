"""
A simple Python/matplotlib implementation of Conway's Game of Life.
Made by: Alan Maldonado
Version: 1.0.0
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
from entities import Entities
from loader import Loader


class GoLSimulation:
    def __init__(self, config: dict, logName="debug_sim.log", grid=np.array([])):
        self.Entities = Entities()
        self.Config = config
        self.Grid = grid
        self.GridSize = 100
        self.FirstPass = True
        # Remove Log File
        try:
            os.remove(logName)
        except:
            pass
        self.LogFile = open(logName, "a+")

    def _ApplyConfiguration(self):
        self.GridSize = self.Config.get("universe_size")
        if self.GridSize == None:
            print(
                "\t[CONFIG_KEY_NOT_FOUND] Universe Size value was set to default (100)")
            self.GridSize = 100
        self.Grid = np.zeros(
            self.GridSize*self.GridSize).reshape(self.GridSize, self.GridSize)

        patterns = self.Config.get("patterns")
        if patterns == None:
            print("\t[CONFIG_KEY_NOT_FOUND] Patterns value was not found")
            sys.exit()
            return self.Grid

        mode = self.Config.get("mode")
        if mode == "txt":
            for pat in patterns:
                x = pat.get("x")
                y = pat.get("y")

                if x > self.GridSize or x < 0:
                    print("\t[PATTERN_COORDS_INVALID] Skipping invalid pattern")
                    continue
                if y > self.GridSize or y < 0:
                    print("\t[PATTERN_COORDS_INVALID] Skipping invalid pattern")
                    continue

                self.Grid[x][y] = 255
        elif mode == "json":
            for pat in patterns:
                patType = pat.get("type")
                if patType == None:
                    print(
                        "\t[PATTERN_TYPE_NOT_FOUND] Skipping incomplete pattern")
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

                if patCordX > (self.GridSize-1) or patCordX < 0 or patCordY > (self.GridSize-1) or patCordY < 0:
                    print(
                        "[INVALID_COORDINATES] Skipping invalid pattern")
                    continue

                # Still Lifes
                if patType == "block":
                    self.Entities.LoadBlock(patCordX, patCordY, self.Grid)
                    continue
                elif patType == "beehive":
                    self.Entities.LoadBeehive(patCordX, patCordY, self.Grid)
                    continue
                elif patType == "loaf":
                    self.Entities.LoadLoaf(patCordX, patCordY, self.Grid)
                    continue
                elif patType == "boat":
                    self.Entities.LoadBoat(patCordX, patCordY, self.Grid)
                    continue
                elif patType == "tub":
                    self.Entities.LoadTub(patCordX, patCordY, self.Grid)
                    continue

                # Oscilators
                if patType == "blinker":
                    self.Entities.LoadBlinker(patCordX, patCordY, self.Grid)
                    continue
                elif patType == "toad":
                    self.Entities.LoadToad(patCordX, patCordY, self.Grid)
                    continue
                elif patType == "beacon":
                    self.Entities.LoadBeacon(patCordX, patCordY, self.Grid)
                    continue

                # Spaceships
                if patType == "Glider":
                    self.Entities.LoadGlider(patCordX, patCordY, self.Grid)
                    continue
                elif patType == "light-weight spaceship":
                    self.Entities.LoadLightWeightSpaceship(
                        patCordX, patCordY, self.Grid)
                    continue
        return

    def StartSimulation(self):
        self._ApplyConfiguration()
        print("[SUCCESS] Started Conway's Game of Life Simulation")

        updateInterval = 1

        # set up animation
        fig, ax = plt.subplots()
        img = ax.imshow(self.Grid, interpolation='nearest')
        ani = animation.FuncAnimation(fig,
                                      self._Update,
                                      fargs=(img, self.GridSize,),
                                      frames=4,
                                      interval=updateInterval,
                                      save_count=50,
                                      repeat=False)
        plt.show()

    def _Update(self, frameNum, img, N):

        newGrid = self.Grid.copy()
        newGrid = self._ApplyRules()

        img.set_data(newGrid)
        self.Grid[:] = newGrid[:]

        tempCheckerGrid = newGrid.copy()

        # print(f"==== FRAME {frameNum}\n")
        if not self.FirstPass:
            self.LogFile.write(f"==== FRAME {frameNum}\n")

        def CheckObject(index: int, pattern: np.array, patternName: str,  tempCheckerGrid: np.array):
            tmpCheck = self._FindIfPatternExists(
                tempCheckerGrid, pattern)
            if tmpCheck[0]:
                # print("\tFound!")
                counter = 0

                def CheckAndRemovePattern(grid: np.array, counter: int, pattern: np.array, upper_left: list) -> (np.array, int):
                    for ul_item in upper_left:
                        ul_row = ul_item[0]
                        ul_col = ul_item[1]
                        b_rows, b_cols = pattern.shape
                        a_slice = grid[ul_row: ul_row + b_rows,
                                       :][:, ul_col: ul_col + b_cols]
                        if a_slice.shape != pattern.shape:
                            continue

                        if (a_slice == pattern).all():
                            counter += 1
                            grid[ul_row: ul_row + b_rows,
                                 :][:, ul_col: ul_col + b_cols] = 0

                    return grid, counter

                res = CheckAndRemovePattern(
                    tempCheckerGrid, counter, pattern, tmpCheck[1])
                tempCheckerGrid, counter = res

                if counter != 0:
                    if not self.FirstPass:
                        self.LogFile.write(
                            f"\t> Grid has {counter} {patternName}(s)\n")

        ents = self.Entities.GetEntities()

        i = 0
        for (name, pattern) in ents:
            # print(f"[{i}]Checking: ", name)
            CheckObject(i, pattern, name, tempCheckerGrid)
            i += 1

        if self.FirstPass:
            self.FirstPass = False
        return img,

    def _ApplyRules(self):
        """Applies the rules to to the grid, and returns the modified/updated grid"""
        updatedGrid = np.zeros(
            self.GridSize*self.GridSize).reshape(self.GridSize, self.GridSize)
        tempGrid = self.Grid.copy()

        for i in range(self.GridSize):
            for j in range(self.GridSize):
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
                    if i != (self.GridSize-1):
                        if tempGrid[i+1][j] >= 255:
                            neiAm += 1

                    # Left
                    if j != 0:
                        if tempGrid[i][j-1] >= 255:
                            neiAm += 1

                    # Right
                    if j != (self.GridSize-1):
                        if tempGrid[i][j+1] >= 255:
                            neiAm += 1

                    # Down Left
                    if i != 0 and j != 0:
                        if tempGrid[i-1][j-1] >= 255:
                            neiAm += 1

                    # Down Right
                    if i != 0 and j != (self.GridSize-1):
                        if tempGrid[i-1][j+1] >= 255:
                            neiAm += 1

                    # Up Right
                    if i != (self.GridSize-1) and j != (self.GridSize-1):
                        if tempGrid[i+1][j+1] >= 255:
                            neiAm += 1

                    # Up Left
                    if i != (self.GridSize-1) and j != 0:
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

                    if i != (self.GridSize-1):
                        if tempGrid[i+1][j] >= 255:
                            neiAm += 1

                    if j != 0:
                        if tempGrid[i][j-1] >= 255:
                            neiAm += 1

                    if j != (self.GridSize-1):
                        if tempGrid[i][j+1] >= 255:
                            neiAm += 1

                    if i != 0 and j != 0:
                        if tempGrid[i-1][j-1] >= 255:
                            neiAm += 1

                    if i != 0 and j != (self.GridSize-1):
                        if tempGrid[i-1][j+1] >= 255:
                            neiAm += 1

                    if i != (self.GridSize-1) and j != (self.GridSize-1):
                        if tempGrid[i+1][j+1] >= 255:
                            neiAm += 1

                    if i != (self.GridSize-1) and j != 0:
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

    def _Check(self, a, b, upper_left):
        ul_row = upper_left[0]
        ul_col = upper_left[1]
        b_rows, b_cols = b.shape
        a_slice = a[ul_row: ul_row + b_rows, :][:, ul_col: ul_col + b_cols]
        if a_slice.shape != b.shape:
            return False
        return (a_slice == b).all()

    def _FindIfPatternExists(self, big_array, small_array) -> (bool, np.array):
        upper_left = np.argwhere(big_array == small_array[0, 0])
        for ul in upper_left:
            if self._Check(big_array, small_array, ul):
                return (True, upper_left)
        else:
            return (False, None)


def main():
    parser = argparse.ArgumentParser(
        description="Runs DrN3MESiS (Alan Maldonado) Implementation of Conway's Game of Life.")
    parser.add_argument(
        "configFilename", help="Filename of the Configuration File")

    args = parser.parse_args()
    if not os.path.isfile(args.configFilename):
        print("[NOT_FOUND] File was not found or is not accessible")
        sys.exit()

    ConfigLoader = Loader(args.configFilename)
    GoL = GoLSimulation(ConfigLoader.GetConfig())
    GoL.StartSimulation()

    GoL.LogFile.close()
    return


# call main
if __name__ == '__main__':
    main()
