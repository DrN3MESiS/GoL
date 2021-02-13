import numpy as np


class Entities:
    def __init__(self):
        self.Block = np.array([[255,    255],
                               [255,  255]])
        self.Beehive = np.array([[0,    255, 255, 0],
                                 [255,  0, 0, 255],
                                 [0,  255, 255, 0]])
        self.Loaf = np.array([[0,    255, 255, 0],
                              [255,  0, 0, 255],
                              [0,  255, 0, 255],
                              [0,  0, 255, 0]])
        self.Boat = np.array([[255,    255, 0],
                              [255,  0, 255],
                              [0,  255, 0]])
        self.Tub = np.array([[0,    255, 0],
                             [255,  0, 255],
                             [0,  255, 0]])
        self.Blinker = np.array([[255, 255, 255]])
        self.BlinkerV2 = np.array([[255], [255], [255]])
        self.Toad = np.array([[0,    0, 255, 0],
                              [255,  0, 0, 255],
                              [255,  0, 0, 255],
                              [0,  255, 0, 0]])
        self.Beacon = np.array([[255, 255, 0, 0],
                                [255, 255, 0, 0],
                                [0,  0, 255, 255],
                                [0,  0, 255, 255]])
        self.Glider = np.array([[0,    0, 255],
                                [255,  0, 255],
                                [0,  255, 255]])
        self.LightWeightSpaceship = np.array([[255, 0, 0, 255, 0],
                                              [0, 0, 0, 0, 255],
                                              [255,  0, 0, 0, 255],
                                              [0,  255, 255, 255, 255]])
        return

    def LoadBlock(self, i, j, grid):
        """adds a Block with top left cell at (i, j)"""
        grid[i: i+2, j: j+2] = self.Block

    def LoadBeehive(self, i, j, grid):
        """adds a Beehive with top left cell at (i, j)"""
        grid[i: i+4, j: j+3] = self.Beehive

    def LoadLoaf(self, i, j, grid):
        """adds a Loaf with top left cell at (i, j)"""
        grid[i: i+4, j: j+4] = self.Loaf

    def LoadBoat(self, i, j, grid):
        """adds a Boat with top left cell at (i, j)"""
        grid[i: i+3, j: j+3] = self.Boat

    def LoadTub(self, i, j, grid):
        """adds a Tub with top left cell at (i, j)"""
        grid[i: i+3, j: j+3] = self.Tub

    # Oscilators

    def LoadBlinker(self, i, j, grid):
        """adds a Blinker with top left cell at (i, j)"""
        grid[i: i+1, j: j+3] = self.Blinker

    def LoadToad(self, i, j, grid):
        """adds a Toad with top left cell at (i, j)"""
        grid[i: i+4, j: j+4] = self.Toad

    def LoadBeacon(self, i, j, grid):
        """adds a Beacon with top left cell at (i, j)"""
        grid[i: i+4, j: j+4] = self.Beacon

    # Spaceships

    def LoadGlider(self, i, j, grid):
        """adds a Glider with top left cell at (i, j)"""
        grid[i: i+3, j: j+3] = self.Glider

    def LoadLightWeightSpaceship(self, i, j, grid):
        """adds a LightWeightSpaceship with top left cell at (i, j)"""
        grid[i: i+4, j: j+5] = self.LightWeightSpaceship
