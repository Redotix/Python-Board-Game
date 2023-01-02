class Tile:
    tileCoords = ()
    tilestandingplayer = None
    tilestandingpiece = None
    tileID = None

    def __init__(self, tileid, cords, ishouse):
        self.tileCoords = cords
        self.tileID = tileid
        self.ishouse = ishouse
