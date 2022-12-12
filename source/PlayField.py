from Tile import *


class PlayField:
    fieldTiles = []
    canvassize = (5, 5)
    dotsize = 70
    fieldincrement = 8
    fieldminsize = 16
    canvasminsize = 5
    border = 2
    maxdotsize = 70
    color = None

    def __init__(self, fieldcolor):
        self.color = fieldcolor
        self.fieldTiles = []
        # for i in range(len(self.playingFieldVar)):
        #     tile = self.Tile(i, self.playingFieldVar[i])
        #     self.fieldTiles.append(tile)

    def generategield(self, extratiles):
        canvassize = self.canvasminsize + (extratiles * 2) + self.border
        self.dotsize = self.maxdotsize / (canvassize / 7)
        self.canvassize = (canvassize, canvassize)
        center = (canvassize / 2) - 0.5
        rightlist = []
        leftlist = []

        for x in range(2 + extratiles):
            rightlist.append((center + 1, center + 2 + extratiles - x))
            leftlist.append((center - 1, center - 2 - extratiles + x))

        for x in range(1 + extratiles):
            rightlist.append((center + 2 + x, center + 1))
            leftlist.append((center - 2 - x, center - 1))

        rightlist.append((center + 2 + extratiles, center))
        leftlist.append((center - 2 - extratiles, center))

        for x in range(2 + extratiles):
            rightlist.append((center + 2 + extratiles - x, center - 1))
            leftlist.append((center - 2 - extratiles + x, center + 1))

        for x in range(1 + extratiles):
            rightlist.append((center + 1, center - 2 - x))
            leftlist.append((center - 1, center + 2 + x))

        rightlist.append((center, center - 2 - extratiles))
        leftlist.append((center, center + 2 + extratiles))

        fulllist = rightlist + leftlist
        for i in range(len(fulllist)):
            tile = Tile(i, fulllist[i])
            self.fieldTiles.append(tile)
