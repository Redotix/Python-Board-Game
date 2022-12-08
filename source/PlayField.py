class PlayField:
    playingFieldVar = []
    fieldTiles = []
    color = None

    def __init__(self, fieldcolor, inputfield):
        self.playingFieldVar = inputfield
        self.color = fieldcolor
        self.fieldTiles = []
        for i in range(len(self.playingFieldVar)):
            tile = self.Tile(i, self.playingFieldVar[i])
            self.fieldTiles.append(tile)

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
