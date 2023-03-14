from Tile import *


class PlayField:
    fieldTiles = []
    canvassize = (5, 5)
    dotsize = 70
    fieldincrement = 8
    fieldminsize = 16
    canvasminsize = 5
    border = 2
    color = "white"

    starthouses = [[], [], [], []]
    endhouses = [[], [], [], []]
    starttileids = []
    decoration = []

    def generatefield(self, extratiles, screensize):
        canvassize = self.canvasminsize + (extratiles * 2) + self.border
        self.dotsize = (screensize / canvassize) - ((screensize / canvassize) / 7)
        self.canvassize = (canvassize + 1, canvassize)
        center = (canvassize / 2) - 0.5
        rightlist = []
        leftlist = []

        for x in range(canvassize):
            for y in range(canvassize):
                self.decoration.append((x, y))

        # generate playing field in the right order and write down the tiles into a list
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
            tile = Tile(i, fulllist[i], False)
            self.fieldTiles.append(tile)

        # create tiles for end houses and put them in a list
        for i in range(extratiles + 1):
            endhousetuples1 = (center, center + extratiles + 1 - i)
            endhousetuples2 = (center, center - extratiles - 1 + i)
            endhousetuples3 = (center + extratiles + 1 - i, center)
            endhousetuples4 = (center - extratiles - 1 + i, center)

            tile1 = Tile(i, endhousetuples1, True)
            tile2 = Tile(i, endhousetuples2, True)
            tile3 = Tile(i, endhousetuples3, True)
            tile4 = Tile(i, endhousetuples4, True)

            self.endhouses[0].append(tile1)
            self.endhouses[1].append(tile2)
            self.endhouses[2].append(tile3)
            self.endhouses[3].append(tile4)

        # create tiles for starting houes in a grid and put them in a list
        for y in range(1 + int(((extratiles / 2) + 0.5))):
            for x in range(1 + int(((extratiles / 2) + 0.5))):
                starthouses1 = (canvassize - 2 - y, canvassize - 2 - x)
                starthouses2 = (1 + y, 1 + x)
                starthouses3 = (canvassize - 2 - y, 1 + x)
                starthouses4 = (1 + y, canvassize - 2 - x)

                tile1 = Tile(1, starthouses1, True)
                tile2 = Tile(1, starthouses2, True)
                tile3 = Tile(1, starthouses3, True)
                tile4 = Tile(1, starthouses4, True)

                self.starthouses[0].append(tile1)
                self.starthouses[1].append(tile2)
                self.starthouses[2].append(tile3)
                self.starthouses[3].append(tile4)

        # put the IDs of starting tiles into a list
        startingtilesdivision = int(len(self.fieldTiles) / 4)
        for i in range(len(self.fieldTiles)):
            self.starttileids.append(self.fieldTiles[i].tileID)
            self.starttileids.append(self.fieldTiles[startingtilesdivision * 2].tileID)
            self.starttileids.append(self.fieldTiles[startingtilesdivision * 1].tileID)
            self.starttileids.append(self.fieldTiles[startingtilesdivision * 3].tileID)
