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

        # Creating the 4 inner corners of the playing field.
        self.fieldTiles.append((center + 1, center + 1))
        self.fieldTiles.append((center - 1, center + 1))
        self.fieldTiles.append((center + 1, center - 1))
        self.fieldTiles.append((center - 1, center - 1))

        # creating extra tiles from the 4 inner corners and extending them outwards.
        for x in range(1 + extratiles):
            self.fieldTiles.append((center + 2 + x, center + 1))
            self.fieldTiles.append((center - 2 - x, center - 1))

            self.fieldTiles.append((center + 2 + x, center - 1))
            self.fieldTiles.append((center - 2 - x, center + 1))

        for y in range(1 + extratiles):
            self.fieldTiles.append((center + 1,  center - 2 - y))
            self.fieldTiles.append((center - 1, center + 2 + y))

            self.fieldTiles.append((center - 1, center - 2 - y))
            self.fieldTiles.append((center + 1, center + 2 + y))

        # Adding last 4 outer tiles to close off the track loop
        self.fieldTiles.append((center + extratiles + 2, center))
        self.fieldTiles.append((center - extratiles - 2, center))
        self.fieldTiles.append((center, center + extratiles + 2))
        self.fieldTiles.append((center, center - extratiles - 2))

    class Tile:
        tileCoords = ()
        tileStanding = None
        tileID = None

        def __init__(self, tileid, cords):
            self.tileCoords = cords
            self.tileID = tileid

        # gives the class a color, this is to determine if a piece is standing on the tile,
        # it also gives us data about what teams piece is currently standing on this tile.
        def movetotile(self, color):
            self.tileStanding = color
