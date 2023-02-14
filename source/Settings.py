class Settings:
    playeramount = None
    pieceamount = None
    extratiles = None
    piececolors = [(68, 85, 242), (235, 235, 52), (40, 237, 47), (240, 38, 38)]
    housecolors = [(43, 55, 166), (153, 153, 35), (22, 130, 26), (148, 24, 24)]
    starttilecolors = [(103, 114, 219), (214, 214, 103), (106, 189, 109), (186, 95, 95)]

    playernames = ["", "", "", ""]

    def __init__(self, playeramount, pieceamount, extratiles):
        self.playeramount = playeramount
        self.pieceamount = pieceamount
        # 16 is minimum, increment size is 8
        self.extratiles = extratiles
