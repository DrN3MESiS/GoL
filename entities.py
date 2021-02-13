import numpy as np


class Entities:
    def __init__(self):
        # Still Lifes
        self.Block = np.array([
            [255,    255],
            [255,  255]
        ])
        self.Beehive = np.array([
            [0,    255, 255, 0],
            [255,  0, 0, 255],
            [0,  255, 255, 0]
        ])
        self.Loaf = np.array([
            [0,    255, 255, 0],
            [255,  0, 0, 255],
            [0,  255, 0, 255],
            [0,  0, 255, 0]
        ])
        self.Boat = np.array([
            [255,    255, 0],
            [255,  0, 255],
            [0,  255, 0]
        ])
        self.Tub = np.array([
            [0,    255, 0],
            [255,  0, 255],
            [0,  255, 0]
        ])
        # Oscilators
        self.BlinkerV1 = np.array([
            [255, 255, 255]
        ])
        self.BlinkerV2 = np.array([
            [255],
            [255],
            [255]
        ])
        self.ToadV1 = np.array([
            [0,    0, 255, 0],
            [255,  0, 0, 255],
            [255,  0, 0, 255],
            [0,  255, 0, 0]
        ])
        self.ToadV2 = np.array([
            [0,  0, 0, 0],
            [0,  255, 255, 255],
            [0,  255, 255, 0],
            [255,  0, 0, 0]
        ])
        self.BeaconV1 = np.array([
            [255, 255, 0, 0],
            [255, 255, 0, 0],
            [0,  0, 255, 255],
            [0,  0, 255, 255]
        ])
        self.BeaconV2 = np.array([
            [255, 255, 0, 0],
            [255, 0, 0, 0],
            [0,  0, 0, 255],
            [0,  0, 255, 255]
        ])
        # SpaceShips
        self.GliderV1 = np.array([
            [0,    0, 255],
            [255,  0, 255],
            [0,  255, 255]
        ])
        self.GliderV2 = np.array([
            [255,  0, 255],
            [0,  255, 255],
            [0,  255, 0]
        ])
        self.GliderV3 = np.array([
            [0,  0, 255],
            [255,  0, 255],
            [0,  255, 255]
        ])
        self.GliderV4 = np.array([
            [255,  0, 0],
            [0,  255, 255],
            [255,  255, 0]
        ])
        self.LightWeightSpaceshipV1 = np.array([
            [255, 0, 0, 255, 0],
            [0, 0, 0, 0, 255],
            [255,  0, 0, 0, 255],
            [0,  255, 255, 255, 255]
        ])
        self.LightWeightSpaceshipV2 = np.array([
            [0, 0, 255, 255, 0],
            [255, 255, 0, 255, 255],
            [255, 255, 0, 255, 0],
            [0, 255, 255, 0, 0]
        ])
        self.LightWeightSpaceshipV3 = np.array([
            [0, 255, 255, 255, 255],
            [255, 0, 0, 0, 255],
            [0, 0, 0, 0, 255],
            [255, 0, 0, 255, 0]
        ])
        self.LightWeightSpaceshipV4 = np.array([
            [0, 255, 255, 0, 0],
            [255, 255, 0, 255, 0],
            [255, 255, 0, 255, 255],
            [0, 0, 255, 255, 0]
        ])
        return

    def GetEntities(self) -> dict():
        ent = {}

        ent["LightWeightSpaceshipV1"] = self.LightWeightSpaceshipV1
        ent["LightWeightSpaceshipV2"] = self.LightWeightSpaceshipV2
        ent["LightWeightSpaceshipV3"] = self.LightWeightSpaceshipV3
        ent["LightWeightSpaceshipV4"] = self.LightWeightSpaceshipV4

        ent["GliderV1"] = self.GliderV1
        ent["GliderV2"] = self.GliderV2
        ent["GliderV3"] = self.GliderV3
        ent["GliderV4"] = self.GliderV4

        ent["BeaconV1"] = self.BeaconV1
        ent["BeaconV2"] = self.BeaconV2

        ent["ToadV1"] = self.ToadV1
        ent["ToadV2"] = self.ToadV2

        ent["BlinkerV1"] = self.BlinkerV1
        ent["BlinkerV2"] = self.BlinkerV2

        ent["Block"] = self.Block
        ent["Beehive"] = self.Beehive
        ent["Loaf"] = self.Loaf
        ent["Boat"] = self.Boat
        ent["Tub"] = self.Tub

        return ent

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
        grid[i: i+1, j: j+3] = self.BlinkerV1

    def LoadToad(self, i, j, grid):
        """adds a Toad with top left cell at (i, j)"""
        grid[i: i+4, j: j+4] = self.ToadV1

    def LoadBeacon(self, i, j, grid):
        """adds a Beacon with top left cell at (i, j)"""
        grid[i: i+4, j: j+4] = self.BeaconV1

    # Spaceships

    def LoadGlider(self, i, j, grid):
        """adds a Glider with top left cell at (i, j)"""
        grid[i: i+3, j: j+3] = self.GliderV1

    def LoadLightWeightSpaceship(self, i, j, grid):
        """adds a LightWeightSpaceship with top left cell at (i, j)"""
        grid[i: i+4, j: j+5] = self.LightWeightSpaceshipV1
