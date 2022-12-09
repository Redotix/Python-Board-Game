class Settings:
    # I am really cool :)
    playeramount = None
    pieceamount = None
    extratiles = None

    def __init__(self, playeramount, pieceamount, extratiles):
        self.playeramount = playeramount
        self.pieceamount = pieceamount
        # 16 is minimum, increment size is 8
        self.extratiles = extratiles
